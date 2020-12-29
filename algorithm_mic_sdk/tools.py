import hashlib
from functools import lru_cache

import requests


def get_md5(data):
    md5_obj = hashlib.md5()
    if not isinstance(data, bytes):
        data = str(data).encode()
    md5_obj.update(data)
    hash_code = md5_obj.hexdigest()
    return hash_code


class FileInfo(object):
    """
    文件对象,在所有需要上传文件的地方,可以通过构建此对象来实现上传功能
    此类可通过如下函数进行初始化:
        若已有在leqi-algo bucket 上的OSS存储文件名,则可使用 for_oss_name 方法构建对象
        若已有在文件的二进制数据,则可使用 for_file_bytes 方法构建对象
        若有可通过指定方法获取文件二进制数据的,则可使用 for_function 方法构建对象
        若已有在文件的可访问url,则可使用 for_url 方法构建对象
    """

    def __init__(self, func):
        """
        文件对象
        @param func:可执行方法,接收 algorithm_mic_sdk.base.AlgoBase 类实例,需要返回文件的二进制数据
        """
        self.func = func

    @lru_cache(maxsize=1)
    def get_oss_name(self, algo_base):
        """
        获取OSS文件名
        """
        return self.func(algo_base)

    @classmethod
    def for_oss_name(cls, oss_name):
        """
        文件来源于已有的OSS文件名
        """
        return cls(lambda algo_base: oss_name)

    @classmethod
    def for_file_bytes(cls, file_bytes):
        """
        文件来源于二进制数据
        """
        return cls(lambda algo_base: algo_base.send_file(file_bytes))

    @classmethod
    def for_function(cls, function, oss_name):
        """
        文件来源于二进制数据,程序会先检测oss_name对应的文件是否存在,若不会存在,再执行function函数获取文件数据并上传
        :param function:获取文件二进制数据的方法
        :param oss_name:文件的名称
        """
        assert callable(function), Exception('function不是可执行对象')
        return cls(lambda algo_base: algo_base.send_file(file_bytes=function, oss_name=oss_name))

    @classmethod
    def for_url(cls, url):
        """
        文件来源于url,若为阿里云华东二区的url,直接交于算法服务器下载,否则由程序先下载,再上传
        """
        if 'oss-cn-shanghai.aliyuncs.com' in url or 'oss-cn-shanghai-internal.aliyuncs.com' in url:
            return cls(lambda algo_base: url)

        def func(algo_base):
            file_bytes = requests.get(url).content
            return algo_base.send_file(file_bytes)

        return cls(func)
