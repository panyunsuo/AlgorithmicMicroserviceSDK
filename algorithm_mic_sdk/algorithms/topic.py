from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class Topic(AlgoBase):
    __algo_name__ = 'topic'

    def __init__(self, auth_info: AuthInfo, file: FileInfo, corners: list, custom_data=None, **kwargs):
        """
        错题本算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ypg3ub
        @param auth_info:个人权限配置参数
        @param file:文件对象,FileInfo对象
        @param corners:区域框坐标
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_file'] = file.get_oss_name(self)
        self.request['corners'] = corners
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
