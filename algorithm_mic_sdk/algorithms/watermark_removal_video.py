from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class WatermarkRemovalVideo(AlgoBase):
    __algo_name__ = 'watermark_removal_video'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, rect: list, suffix='', **kwargs):
        """
        视频去水印
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ltcypw
        @param auth_info:个人权限配置参数
        @param oss_file:需要去水印的视频
        @param rect:坐标列表[x0, y0, x1, y1]
        @param suffix:后缀
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file.get_oss_name(self)
        self.request['rect'] = rect
        self.request['suffix'] = suffix
        self.request.update(kwargs)
