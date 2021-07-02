from ..auth import AuthInfo
from ..base import AlgoBase


class SpeechSynthesis(AlgoBase):
    __algo_name__ = 'speech_synthesis'

    def __init__(self, auth_info: AuthInfo, text, language, custom_data=None, **kwargs):
        """
        语音合成算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/kynn5m
        @param auth_info:个人权限配置参数
        @param text:待合成文本
        @param language:语言 chinese or english
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['text'] = text
        self.request['language'] = language
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
