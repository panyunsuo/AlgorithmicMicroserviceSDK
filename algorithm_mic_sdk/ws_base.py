"""
WebSocket客户端基类
请求流程为:
    注册+环境初始化-->发送流数据->结束
"""
import _thread as thread
import json
from functools import lru_cache
from urllib.parse import urljoin

import websocket

from algorithm_mic_sdk.auth import AuthInfo


class WSBase(object):

    def __init__(self, auth_info: AuthInfo):
        self._host = auth_info.host
        self._user_name = auth_info.user_name
        self._extranet = auth_info.extranet
        self._password = auth_info.password
        self._random_name = auth_info.random_name
        self._auth_info = auth_info

    def set_on_open(self, on_open):
        self.ws_con.on_open = on_open

    def set_on_message(self, on_message):
        self.ws_con.on_message = on_message

    @property
    @lru_cache(maxsize=1)
    def ws_con(self):
        return websocket.WebSocketApp(urljoin(self._host, '/ws/algorithm'))

    def run(self):
        """
        连接服务器
        @return:
        """
        self.ws_con.run_forever()


class WSAlgoBase(WSBase):
    __algo_name__ = None

    def __init__(self, auth_info: AuthInfo):
        super().__init__(auth_info)
        self.algo_name = self.__algo_name__
        self.request = {}

    def set_on_open(self, on_open):
        def _on_open(ws):
            ws.send(json.dumps(self.initialization_parameters))
            on_open(ws)

        thread.start_new_thread(_on_open, ())

    @property
    def initialization_parameters(self):
        """
        生成算法请求的json参数
        :return: dict
        """
        return {'user_name': self._user_name,
                'password': self._password,
                'target': self.algo_name,
                'request_body': self.request}
