from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class WatermarkRemoval(AlgoBase):
    __algo_name__ = 'watermark_removal'

    def __init__(self, auth_info: AuthInfo, file: FileInfo, rect: list = None, mask: FileInfo = None, **kwargs):
        """
        图片视频去水印
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/fkbzx3
        @param auth_info:个人权限配置参数
        @param file:需要去水印的图片,格式为FileInfo对象
        @param rect:坐标列表[x0, y0, x1, y1]
        """
        super().__init__(auth_info)
        self.request['oss_file'] = file.get_oss_name(self)
        self.request['rect'] = rect
        if mask:
            self.request['mask'] = mask.get_oss_name(self)
        self.request.update(kwargs)
