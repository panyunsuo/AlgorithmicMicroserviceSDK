from ..auth import AuthInfo
from ..base import AlgoBase


class PaperRotation(AlgoBase):
    __algo_name__ = 'paper_rotation'

    def __init__(self, auth_info: AuthInfo, topic_oss_list_files: list, answer_oss_list_files: list, custom_data=None,
                 **kwargs):
        """
        错题本试卷旋转算法
            文档见 https://www.yuque.com/fenfendeyouzhiqingnian/algorithm/ge86ra
        @param auth_info:个人权限配置参数
        @param topic_oss_list_files:文件对象列表,[[FileInfo, FileInfo...],[FileInfo,FileInfo...]]
        @param answer_oss_list_files:文件对象列表,[[FileInfo, FileInfo...],[FileInfo,FileInfo...]]
        @param custom_data:自定义参数,将会随着响应参数原样返回
        """
        super().__init__(auth_info)
        _topic_oss_list_files = []
        for topic_oss_files in topic_oss_list_files:
            _topic_oss_list_files.append([])
            for topic_oss_file in topic_oss_files:
                _topic_oss_list_files[-1].append(topic_oss_file.get_oss_name(self))

        _answer_oss_list_files = []
        for answer_oss_files in answer_oss_list_files:
            _answer_oss_list_files.append([])
            for answer_oss_file in answer_oss_files:
                _answer_oss_list_files[-1].append(answer_oss_file.get_oss_name(self))
        self.request['topic_oss_list_files'] = _topic_oss_list_files
        self.request['answer_oss_list_files'] = _answer_oss_list_files
        self.request['custom_data'] = custom_data
        self.request.update(kwargs)
