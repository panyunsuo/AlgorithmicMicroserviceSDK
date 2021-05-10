"""
@File    :   auth_info.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/21 10:47
"""
import logging


class AuthInfo(object):

    def __init__(self, host, user_name, password, extranet=False, gateway_cache=True, random_name=False):
        """
        账号验证
        :param host:服务器地址 例如:http://gateway.algo.leqi.us
        :param user_name: 算法账号名
        :param password: 算法密码
        :param extranet: 是否使用外网传输图片文件
        :param gateway_cache: 是否需要网关平台使用缓存
        :param random_name: 若为True,在每次请求时,即使是同一文件,也需要重新上传,这样不便于服务器使用缓存
        """
        self.host = host
        self.user_name = user_name
        self.extranet = extranet
        self.password = password
        self.gateway_cache = gateway_cache
        self.random_name = random_name
        if self.extranet:
            logging.warning('AuthInfo 在生产环境下 extranet=True 会加大带宽损耗及降低运行速度,请慎用')

        if not self.gateway_cache:
            logging.warning('AuthInfo 除非你有特殊需求,否则请保持 gateway_cache=True 这对一些情况下的请求具有明显加速效果')

        if random_name:
            logging.warning('AuthInfo 除非你有特殊需求 否则请保持 random_name=False 这会可以避免文件的重复上传')
