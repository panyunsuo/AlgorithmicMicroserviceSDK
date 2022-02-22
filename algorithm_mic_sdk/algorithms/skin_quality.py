from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class SkinQuality(AlgoBase):
    __algo_name__ = 'skin_quality'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, faces: list, custom_data=None, interface_version='V1',
                 **kwargs):
        """
        错题本算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/vc8dlg
        @param auth_info:个人权限配置参数
        @param file:文件对象,FileInfo对象
        @param faces:faces
        @param interface_version:接口版本号,默认为V1
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file.get_oss_name(self)
        self.request['faces'] = faces
        self.request['custom_data'] = custom_data
        self.request['interface_version'] = interface_version
        self.request.update(kwargs)
