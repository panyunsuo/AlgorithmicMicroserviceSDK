import logging
import time
import uuid
from functools import lru_cache
from urllib.parse import urljoin

from . import error
from .auth import AuthInfo
from .error import TaskTimeoutNotCompleted
from .response import Response
from .tools import get_md5, FileInfo


class Base(object):
    """
        基础库,封装了一些基础的函数,例如图片上传 下载 生成预览url 根据任务ID获取结果等,可以单独初始化此库来使用上述功能
        """

    def __init__(self, auth_info: AuthInfo):
        self._host = auth_info.host
        self._user_name = auth_info.user_name
        self._extranet = auth_info.extranet
        self._password = auth_info.password
        self._random_name = auth_info.random_name
        self._auth_info = auth_info

    @property
    @lru_cache(maxsize=1)
    def api_oss_url(self):
        """
        网关平台上传文件的url
        :return:url
        """
        api = 'api/oss/url'
        return urljoin(self._host, api)

    @property
    @lru_cache(maxsize=1)
    def api_async_url(self):
        """
        网关平台异步请求算法的url
        :return:url
        """
        api = 'api/algorithm'
        return urljoin(self._host, api)

    @property
    @lru_cache(maxsize=1)
    def api_task_id_url(self):
        """
        网关平台获取任务结果的url
        :return:url
        """
        api = 'api/algorithm/task/{task_id}'
        return urljoin(self._host, api)

    @lru_cache(maxsize=100)
    def get_put_url(self, oss_name, extranet, headers, timeout):
        allot_data = {'user_name': self._user_name, 'password': self._password, 'filename': oss_name,
                      'extranet': extranet,
                      'headers': headers,
                      'timeout': timeout}
        resp = Response.request('POST', self.api_oss_url, json=allot_data)

        return resp.json['put_url'], resp.json.get('exist_file'), resp.json['oss_name']

    @lru_cache(maxsize=100)
    def _get_file_url(self, oss_name, extranet, watermark, timeout):
        params = {'filename': oss_name, 'extranet': extranet, 'watermark': watermark, 'timeout': timeout}
        resp = Response.request('GET', self.api_oss_url, params=params)
        return resp.json['preview_url']

    def send_file(self, file_bytes, oss_name=None, cover=False, extranet=None, random_name=None, prefix=''):
        """
        上传文件到算法的oss中
        :param file_bytes:文件二进制数据
        :param oss_name: 指定的oss文件名称,若为None则会使用文件md5来命名(此处的文件名不是最终的文件名)
        :param cover: 当该文件名在oss上存在时,是否需要重新上传,覆盖该文件
        :param extranet: 是否使用外网传输, 为None时将使用auth_info中的参数
        :param random_name: 是否随机名称
        :param prefix: 文件名前缀
        :return: 文件在oss上面的文件名
        """
        if extranet is None:
            extranet = self._extranet

        if random_name:
            random_name = self._random_name

        if not oss_name:
            if random_name:
                oss_name = str(uuid.uuid1())
            else:
                oss_name = get_md5(file_bytes)
        oss_name = prefix + oss_name
        put_url, exist_file, oss_name = self.get_put_url(oss_name, extranet, headers=None, timeout=600)

        if not exist_file or cover:
            if callable(file_bytes):
                file_bytes = file_bytes()
            resp = Response.request('PUT', put_url, data=file_bytes, timeout=10)
        return oss_name

    def get_file(self, oss_name=None, extranet=None, watermark=None):
        """
        下载文件数据
        :param oss_name:文件在阿里云oss上的名称
        :param extranet: 是否使用外网传输, 为None时将使用auth_info中的参数
        :param watermark: 是否需要添加水印
        :return: 图片二进制数据
        """
        if extranet is None:
            extranet = self._extranet
        get_url = self._get_file_url(oss_name, extranet, watermark=watermark, timeout=600)
        resp = Response.request('GET', get_url, timeout=10)
        return resp.content

    @lru_cache(maxsize=100)
    def get_file_url(self, oss_name, extranet=False, watermark=None, timeout=3600):
        """
        生成文件的预览地址
        :param oss_name: 文件在阿里云oss上的名称
        :param extranet: 是否使用内网传输, 为None时将使用auth_info中的参数
        :param watermark: 图片水印
        :param timeout: 预览鱼片过期时间
        :return: url
        """
        if extranet is None:
            extranet = self._extranet
        get_url = self._get_file_url(oss_name, extranet, watermark, timeout)
        return get_url

    def get_results(self, task_id):
        """
        根据任务ID获取处理结果,未处理完成时resp.allot_code=501
        :param task_id: 任务ID
        :return: algorithm.response.Response
        """
        url = self.api_task_id_url.format(task_id=task_id)
        resp = Response.request('GET', url)
        return resp


class AlgoBase(Base):
    """
    各个算法的基类,通过继承此模块,拥有生成算法参数,请求算法等功能
    """
    __algo_name__ = None

    def __init__(self, auth_info: AuthInfo):
        super().__init__(auth_info)
        self.algo_name = self.__algo_name__
        self.gateway_cache = auth_info.gateway_cache
        self.request = {}

    @property
    def json(self):
        """
        生成算法请求的json参数
        :return: dict
        """
        return {'user_name': self._user_name,
                'password': self._password,
                'target': self.algo_name,
                'gateway_cache': self.gateway_cache,
                'request': self.request}

    def synchronous_request(self, timeout=30, interval=0.5):
        """
        同步请求算法(实质上是多次异步请求)
        :param timeout:请求超时时间
        :param interval: 每次轮询的间隔
        :return:algorithm.response.Response
        """
        stop_time = time.time() + timeout
        # 发布任务
        task_id = self.asynchronous_request().task_id
        while time.time() < stop_time:
            try:
                response = self.get_results(task_id)
            except Exception:
                logging.exception('同步请求算法 获取结果异常 重试')
                response = None
            if response:
                if response.gateway_code == 1000:
                    return response
                elif response.gateway_code != 1002:
                    raise error.AlgorithmProcessingFailed(response.gateway_code, response.gateway_error)
            time.sleep(interval)

        raise TaskTimeoutNotCompleted(task_id, timeout, interval)

    def asynchronous_request(self):
        """
        异步发布算法
        :return:algorithm.response.Response
        """
        response = Response.request('POST', self.api_async_url, json=self.json)
        return response

    def file_auto_process(self, file_info, has_none=None):
        """
        文件自动处理,若传入的
        :param file_info:文件,FileInfo对象或者为oss文件名的字符串
        :param has_none:是否可以为None
        :return:str:oss文件名
        """
        if not file_info:
            if has_none:
                return None
            else:
                raise TypeError('参数不得为空')
        if isinstance(file_info, str):
            return file_info
        elif isinstance(file_info, FileInfo):
            return file_info.get_oss_name(self)
        else:
            raise error.UnknownType(type(file_info))
