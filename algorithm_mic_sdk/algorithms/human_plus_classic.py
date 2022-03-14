from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class HumanPlusClassic(AlgoBase):
    __algo_name__ = 'human_plus'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, cut_params=None, need_to_use_cache=True,
                 just_one_face=False, need_feature_info=False, need_all_face=False, **kwargs):
        """
        半身照/全身照算法
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/mm656w
        @param auth_info:
        @param oss_file: 文件名
        @param process:缩放参数
        @param cut_params:裁剪参数
        @param need_to_use_cache:是否需要使用缓存
        @param just_one_face:是否只处理一张人脸的情况
        @param need_feature_info:是否需要人脸特征点信息
        @param need_all_face:是否需要所有的人脸图片
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request['cut_params'] = cut_params
        self.request['need_to_use_cache'] = need_to_use_cache
        self.request['just_one_face'] = just_one_face
        self.request['need_feature_info'] = need_feature_info
        self.request['need_all_face'] = need_all_face
        self.request.update(kwargs)
