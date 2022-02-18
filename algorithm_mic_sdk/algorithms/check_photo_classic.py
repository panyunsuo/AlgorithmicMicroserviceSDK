from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class CheckPhotoClassic(AlgoBase):
    __algo_name__ = 'check_photo'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, specRule: dict = False,
                 result_matches: bool = False, need_resize_parameters: bool = True, **kwargs):
        """
        合规检测算法
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/mcreye
        @param auth_info:
        @param oss_file: 原图
        @param process: 缩放参数
        @param specRule: 规格参数
        @param result_matches: 是否需要结果匹配
        @param need_resize_parameters: 是否需要重整后的参数
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request['specRule'] = specRule
        self.request['result_matches'] = result_matches
        self.request['need_resize_parameters'] = need_resize_parameters
        self.request.update(kwargs)
