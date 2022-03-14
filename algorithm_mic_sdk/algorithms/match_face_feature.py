from ..auth import AuthInfo
from ..base import AlgoBase
from ..tools import FileInfo


class MatchFaceFeatureV2(AlgoBase):
    __algo_name__ = 'match_face_feature_v2'
    _has_classic = True

    def __init__(self, auth_info: AuthInfo, target_features, filter_features_file: FileInfo = None,
                 filter_features_list: list = None, reference_similarity=None, **kwargs):
        """
        人脸特征匹配算法V2(目前用于考勤项目)
            文档地址: https://www.yuque.com/fenfendeyouzhiqingnian/algo/nou3ac
        @param auth_info:
        @param target_features: 目标特征值的base64数据
        @param filter_features_file:上传到阿里云oss2 上 testleqi 中的待匹配特征值的json文件,其格式见filter_features_list说明
        @param filter_features_list:待匹配特征值列表
        @param reference_similarity:参照的相似度
        @param kwargs:
        """
        super().__init__(auth_info)
        self.request['target_features'] = target_features
        self.request['filter_features_file'] = filter_features_file
        self.request['filter_features_list'] = filter_features_list
        self.request['reference_similarity'] = reference_similarity
        self.request.update(kwargs)
