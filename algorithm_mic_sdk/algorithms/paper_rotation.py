from ..auth import AuthInfo
from ..base import AlgoBase


class PaperRotation(AlgoBase):
    __algo_name__ = 'paper_rotation'

    def __init__(self, auth_info: AuthInfo, files: list, custom_data=None, **kwargs):
        """
        错题本试卷旋转算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ge86ra
        @param auth_info:个人权限配置参数
        @param files:文件对象列表,FileInfo对象
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_files'] = [file.get_oss_name(self) for file in files]
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
