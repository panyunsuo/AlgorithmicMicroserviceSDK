from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class ImageHandleClassic(AlgoBase):
    __algo_name__ = 'image_handle'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, person_info: bool = False,
                 crop_params: dict = None, scaling_parameters: dict = None, person_label: bool = False,
                 img_format='PNG', **kwargs):
        """
        图片预处理
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/rkgppk
        @param auth_info:
        @param oss_file: 待处理的图片信息
        @param process: 原图预缩放参数
        @param person_info: 是否需要人体信息
        @param crop_params: 裁剪参数
        @param scaling_parameters:缩放参数
        @param person_label: 是否需要分割图
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['file'] = oss_file
        self.request['process'] = process
        self.request['person_info'] = person_info
        self.request['crop_params'] = crop_params
        self.request['scaling_parameters'] = scaling_parameters
        self.request['person_label'] = person_label
        self.request['img_format'] = img_format
        self.request.update(kwargs)
