from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class WeddingPhotoClassic(AlgoBase):
    __algo_name__ = 'wedding_photo'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process=None, img_size: list = None,
                 beauty_level_right: dict = None, beauty_level_left: dict = None, need_beauty_buffer: bool = False,
                 use_cache: bool = True, **kwargs):
        """
        结婚照制作
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/sla5g1
        @param auth_info:
        @param oss_file: 原图
        @param process: 缩放参数
        @param img_size: 结果图尺寸
        @param beauty_level_right: 右脸美颜参数
        @param beauty_level_left: 左脸美颜参数
        @param need_beauty_buffer: 是否需要人脸美颜的缓存参数,此参数可以用于本地美颜
        @param use_cache: 是否需要缓存
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['oss_file'] = oss_file
        self.request['process'] = process
        self.request['img_size'] = img_size
        self.request['beauty_level_right'] = beauty_level_right
        self.request['beauty_level_left'] = beauty_level_left
        self.request['need_beauty_buffer'] = need_beauty_buffer
        self.request['use_cache'] = use_cache
        self.request.update(kwargs)

