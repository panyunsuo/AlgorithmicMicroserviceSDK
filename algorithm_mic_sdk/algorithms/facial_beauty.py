from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class FacialBeauty(AlgoBase):
    __algo_name__ = 'facial_beauty_v2'

    def __init__(self, auth_info: AuthInfo, file: FileInfo, texture_degree=1, whitening=False,  process=None, custom_data=None,
                 **kwargs):
        """
        人像美颜算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ocs8mclb54goy00e
        @param auth_info:个人权限配置参数
        @param file:文件对象,FileInfo对象
        @param texture_degree:加纹理的控制参数，在0-3之间选择，越大代表加纹理程度越大
        @param whitening:是否要美白
        @param process:缩放规则
        @param single:默认为False
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_file'] = file.get_oss_name(self)
        self.request['process'] = process
        self.request['texture_degree'] = texture_degree
        self.request['whitening'] = whitening
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
