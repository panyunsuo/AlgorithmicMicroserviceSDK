from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class GPUAccelerate(AlgoBase):
    __algo_name__ = 'gpu_accelerate'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, params, **kwargs):
        """
        证件照GPU阶段性加速算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/hzc04p
        @param auth_info:个人权限配置参数
        @param oss_file:文件对象,FileInfo对象
        @param params:配置参数
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file.get_oss_name(self)
        self.request['params'] = params
        self.request.update(kwargs)
