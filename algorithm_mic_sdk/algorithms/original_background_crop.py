from ..base import AlgoBase
from ..tools import FileInfo


class OriginalBackgroundCrop(AlgoBase):
    __algo_name__ = 'original_background_crop'
    _has_classic = True

    def __init__(self, auth_info, oss_file: FileInfo, spec_info: dict, process=None,
                 cutout_cache=True, **kwargs):
        """
        证件照带原背景的裁剪算法
        :param auth_info:验证参数
        :param oss_file:图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        :param spec_info:规格参数
        :param process:原图缩放参数
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request['spec_info'] = spec_info
        self.request['cutout_cache'] = cutout_cache
        self.request.update(kwargs)
