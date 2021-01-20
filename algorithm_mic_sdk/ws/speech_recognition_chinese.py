import base64
import json

from ..auth import AuthInfo
from ..ws_base import WSAlgoBase


def build_data_stream_source(data_stream_iterator):
    def on_open(ws):
        for stream in data_stream_iterator:
            if isinstance(stream, bytes):
                part = base64.b64encode(stream).decode()
            else:
                part = stream
            data = {
                'state': 'running',
                'part': part
            }
            ws.send(json.dumps(data))
        ws.send(json.dumps({'state': 'end'}))

    return on_open


class SpeechRecognitionChinese(WSAlgoBase):
    __algo_name__ = 'speech_recognition_chinese'

    def __init__(self, auth_info: AuthInfo, audio_format='PCM', data_stream_iterator=None,
                 recognition_result_callback_func=None, minimum_segment_frame=None, minimum_valid_frame=None,
                 maximum_audio_segment=None, **kwargs):
        """
        语音识别算法(中文)
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/kbmfrx
        @param auth_info:个人权限配置参数
        @param audio_format:音频格式
        @param data_stream_iterator: 数据流的可迭代对象,可以通过for循环来获得数据流,数据流可以是字节,也可以是base64编码后的数据
        @param recognition_result_callback_func: 识别结果回调函数,该函数接收两个参数 (ws, data)
                其中,ws为当前连接的WebSocket句柄,data为服务器返回的结果
        @param minimum_valid_frame:最小的可识别的有效帧数量
        @param minimum_segment_frame:用来分段的最小的静音帧数量
        @param maximum_audio_segment:最大分段长度,大于此长度的段,将自动进行分段操作
        @param kwargs:
        """

        super().__init__(auth_info)
        self.request['audio_format'] = audio_format
        self.request['minimum_segment_frame'] = minimum_segment_frame
        self.request['minimum_valid_frame'] = minimum_valid_frame
        self.request['maximum_audio_segment'] = maximum_audio_segment
        self.request['state'] = 'ready'
        self.request.update(kwargs)
        self.set_on_message(recognition_result_callback_func)
        self.set_on_open(build_data_stream_source(data_stream_iterator))
