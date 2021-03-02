from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class SpeechRecognitionChinese(AlgoBase):
    __algo_name__ = 'speech_recognition_chinese'

    def __init__(self, auth_info: AuthInfo, file: FileInfo, audio_format='PCM', lm_weight=None, **kwargs):
        """
        语音识别算法(中文)
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/kbmfrx
        @param auth_info:个人权限配置参数
        @param file:需要识别的音频,格式为FileInfo对象
        @param audio_format:音频格式
        @param lm_weight:语言模型的权重
        """
        super().__init__(auth_info)
        self.request['oss_file'] = file.get_oss_name(self)
        self.request['audio_format'] = audio_format
        self.request['lm_weight'] = lm_weight
        self.request.update(kwargs)
