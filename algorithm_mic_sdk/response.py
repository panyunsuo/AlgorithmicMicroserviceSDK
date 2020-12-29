from functools import lru_cache

from requests import Session

from . import error

sess = Session()


class Response(object):

    def __init__(self, resp):
        self.resp = resp
        if self.resp.status_code == 403:
            raise error.AbnormalAlgorithmPlatform(self.resp.status_code, self.json['error'])
        elif self.resp.status_code != 200:
            raise error.AbnormalAlgorithmPlatform(self.resp.status_code, self.text)

    @classmethod
    def request(cls, method, url, *args, **kwargs):
        return cls(sess.request(method, url, *args, **kwargs))

    @property
    @lru_cache(maxsize=1)
    def json(self):
        """
        响应数据的dict类型数据
        :return: dict
        """

        try:
            return self.resp.json()
        except Exception:
            raise error.CannotBeConvertedToJSON(self.resp.text)

    @property
    def text(self):
        """
        响应数据的文本数据
        :return: str
        """
        return self.resp.text

    @property
    def content(self):
        """
        响应数据的二进制数据
        :return: bytes
        """
        return self.resp.content

    @property
    def gateway_code(self):
        """
        网关平台响应码
        :return: int
        """
        return self.json.get('gateway_code', 1000)

    @property
    def gateway_use_cache(self):
        """
        网关平台是否使用了缓存,在根据任务ID获取任务结果时有意义
        :return: bool
        """
        return self.json.get('gateway_cache', False)

    @property
    def gateway_task_id(self):
        """
        获取task id ,只有算法发布成功后才有此数据
        :return: str
        """
        return self.json.get('task_id')

    @property
    def gateway_error(self):
        """
        网关平台错误信息,可能为None
        :return: str
        """
        return self.json.get('error')

    @property
    def task_id(self):
        return self.json.get('task_id')

    @property
    @lru_cache(maxsize=1)
    def result(self):
        """
        算法响应结果(只有gateway_code=200时有效)
        @return:
        """
        return self.json.get('result')

    @property
    def algo_server_timing(self):
        """
        算法响应时间(s )(只有gateway_code=200时有效)
        :return: float
        """
        return self.result.get('algo_server_timing')

    @property
    def custom_data(self):
        """
        算法请求时自定义的数据(只有gateway_code=200时有效)
        """
        return self.result.get('custom_data')

    @property
    def message(self):
        """
        算法返回信息,可能为None(只有gateway_code=200时有效)
        :return: str
        """
        return self.result.get('message')

    @property
    def code(self):
        """
        算法本身的异常信息(只有gateway_code=200时有效)
        :return: str
        """
        return self.result.get('code')
