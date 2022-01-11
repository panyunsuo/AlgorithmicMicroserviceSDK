from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class FaceInfoClassic(AlgoBase):
    __algo_name__ = 'face_info'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, **kwargs):
        """
        获取人脸信息
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/zk78z1
        @param auth_info:
        @param oss_file: 待识别的图片信息
        @param process: 原图预缩放参数
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request.update(kwargs)
