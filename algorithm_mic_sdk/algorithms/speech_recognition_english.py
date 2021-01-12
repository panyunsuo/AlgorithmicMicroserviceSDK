from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class SpeechRecognitionEnglish(AlgoBase):
    __algo_name__ = 'speech_recognition_english'

    def __init__(self, auth_info: AuthInfo, file: FileInfo, text=None, **kwargs):
        """
        语音识别算法(英语)
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/sueme3
        @param auth_info:个人权限配置参数
        @param file:需要识别的音频,格式为FileInfo对象
        @param text:匹配的字符串
        """
        super().__init__(auth_info)
        self.request['oss_file'] = file.get_oss_name(self)
        self.request['text'] = text
        self.request.update(kwargs)
