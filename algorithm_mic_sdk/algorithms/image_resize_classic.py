from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class ImageResizeClassic(AlgoBase):
    __algo_name__ = 'image_resize'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, size, sharp=True, mode=0, img_format='JPEG', **kwargs):
        """
        图片缩放算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algo/kipq9c
        @param auth_info:个人权限配置参数
        @param oss_file:文件对象,FileInfo对象
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['size'] = size
        self.request['sharp'] = sharp
        self.request['mode'] = mode
        self.request['img_format'] = img_format
        self.request.update(kwargs)
