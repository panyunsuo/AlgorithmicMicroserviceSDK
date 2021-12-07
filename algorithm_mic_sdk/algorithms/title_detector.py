from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class TitleDetector(AlgoBase):
    __algo_name__ = 'title_detector'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, custom_data=None, **kwargs):
        """
        标题检测算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/vbegaa
        @param auth_info:个人权限配置参数
        @param oss_file:文件对象,FileInfo对象
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file.get_oss_name(self)
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
