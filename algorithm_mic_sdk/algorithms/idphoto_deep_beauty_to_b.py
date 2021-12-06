from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class IDPhotoDeepBeautyToB(AlgoBase):
    __algo_name__ = 'idphoto_deep_beauty_to_b'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, spec_info: dict = None,
                 deep_beauty_template: str = None, **kwargs):
        """
        证件照B端精修美颜
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/rzpvyr
        @param auth_info:
        @param file:图片文件 可以是str:oss文件名 bytes:原图字节文件 PIL.Image.Image:PIL图片对象  algorithm.ExecutableFunction对象
        @param process:原图缩放参数
        @param spec_info: 规格参数
        @param deep_beauty_template: 模板名称
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file.get_oss_name(self)
        self.request['process'] = process
        self.request['spec_info'] = spec_info
        self.request['deep_beauty_template'] = deep_beauty_template
        self.request.update(kwargs)


class IDPhotoDeepBeautyToBClassic(IDPhotoDeepBeautyToB):
    __algo_name__ = 'idphoto_deep_beauty_to_b'
    _has_classic = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
