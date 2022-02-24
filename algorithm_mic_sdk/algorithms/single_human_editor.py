from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class SingleHumanEditor(AlgoBase):
    __algo_name__ = 'single_human_editor'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, beauty_level=None, deep_beauty_template=None,
                 gpu_deep_beauty=True, clothes_oss_file: FileInfo = None, use_cache=True, process=None, **kwargs):
        """
        单人人像编辑
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/cd5nqs
        @param auth_info:
        @param oss_file:待处理图片
        @param beauty_level: 基础美颜级别
        @param deep_beauty_template: 精修美颜模板
        @param gpu_deep_beauty: 是否使用GPU加速精修
        @param clothes_oss_file: 服装模板信息
        @param use_cache:是否使用缓存
        @param process:缩放参数
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request['beauty_level'] = beauty_level
        self.request['deep_beauty_template'] = deep_beauty_template
        self.request['gpu_deep_beauty'] = gpu_deep_beauty
        self.request['clothes_oss_file'] = clothes_oss_file
        self.request['use_cache'] = use_cache
        self.request.update(kwargs)
