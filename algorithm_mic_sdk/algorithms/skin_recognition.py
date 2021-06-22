from typing import List

from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class SkinRecognition(AlgoBase):
    __algo_name__ = 'skin_recognition'

    def __init__(self, auth_info: AuthInfo, oss_files: List[FileInfo], process=None, continue_to_monitor=None,
                 custom_data=None,
                 **kwargs):
        """
        医疗皮肤监测算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/rogtxc
        @param auth_info:个人权限配置参数
        @param oss_files:文件对象列表,FileInfo对象列表
        @param process:缩放参数
        @param continue_to_monitor:算法有两种检测模式,此处指定的是当第一种未检测出结果是是否使用第二种检测方式,默认为True
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        self.request['oss_files'] = [file.get_oss_name(self) for file in oss_files]
        self.request['custom_data'] = custom_data
        self.request['process'] = process
        self.request['continue_to_monitor'] = continue_to_monitor
        self.request.update(kwargs)
