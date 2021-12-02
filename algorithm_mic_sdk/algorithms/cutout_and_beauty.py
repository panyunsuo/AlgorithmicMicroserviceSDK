from typing import List

from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class CutoutAndBeauty(AlgoBase):
    __algo_name__ = 'cutout_and_beauty'

    def __init__(self, auth_info: AuthInfo, oss_file: FileInfo, process: str = '', spec_info: dict = None,
                 beauty_level: dict = None, clothes_keys: List[FileInfo] = None, save_pack_data: bool = True,
                 has_full_body_dress_up: bool = False, collar_coordinates: dict = None,
                 need_original_background: bool = False, hat_img: FileInfo = None, hat_params: dict = None,
                 need_adjust_lighting: bool = False, enhanced_type: str = 'NOT_ENHANCED', hor_align_type: int = 0,
                 deep_beauty: int = 0, deep_beauty_template: str = None, **kwargs):
        """
        证件照制作+换装+精修(GPU)
            文档地址:https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ucgybr
        @param auth_info: 权限配置参数
        @param oss_file:待处理的原图
        @param process:原图缩放参数
        @param spec_info:规格参数
        @param beauty_level:美颜参数
        @param clothes_keys:服装列表,不传表示不换装
        @param save_pack_data:是否需要换装中间结果
        @param has_full_body_dress_up:是否需要全身换装
        @param collar_coordinates:手动衣服模板衣领坐标
        @param need_original_background:是否需要原图背景
        @param hat_img:帽子图片信息
        @param hat_params:帽子的特征点参数
        @param need_adjust_lighting:need_adjust_lighting
        @param enhanced_type:图像增强控制参数
        @param hor_align_type:裁剪方式
        @param deep_beauty:是否需要精修美颜
        @param deep_beauty_template:精修美颜的模板
        @param kwargs:补充参数
        """
        super().__init__(auth_info)
        self.request["oss_file"] = oss_file
        self.request["process"] = process
        self.request["spec_info"] = spec_info
        self.request["beauty_level"] = beauty_level
        self.request["clothes_keys"] = clothes_keys
        self.request["save_pack_data"] = save_pack_data
        self.request["has_full_body_dress_up"] = has_full_body_dress_up
        self.request["collar_coordinates"] = collar_coordinates
        self.request["need_original_background"] = need_original_background
        self.request["hat_img"] = hat_img
        self.request["hat_params"] = hat_params
        self.request["need_adjust_lighting"] = need_adjust_lighting
        self.request["enhanced_type"] = enhanced_type
        self.request["hor_align_type"] = hor_align_type
        self.request["deep_beauty"] = deep_beauty
        self.request["deep_beauty_template"] = deep_beauty_template
        self.request.update(kwargs)
