"""
@File    :   error.py
@Contact :   panrs@venpoo.com

@Modify Time
------------
2020/4/20 13:17
"""


class CustomException(Exception):
    name = '异常'

    def __init__(self, *args, **kwargs):
        self._error = self.name + '\t'
        if args:
            self._error += str(args)
        if kwargs:
            self._error += '\t' + str(kwargs)

    def __str__(self):
        return self._error


class UnknownType(CustomException):
    name = '未知参数类型'


class CannotBeConvertedToJSON(CustomException):
    name = '无法转换数据为JSON'


class TaskTimeoutNotCompleted(CustomException):
    name = '任务超时未完成'


class AlgorithmProcessingFailed(CustomException):
    name = '算法处理失败'


class AbnormalAlgorithmPlatform(CustomException):
    """
    算法平台异常 一般只会在开发阶段出现,一旦开发阶段调通后就不会出现该异常
    """
    code = 403
    name = '算法平台异常'

    def __init__(self, code, error, *args):
        super().__init__(code, error, *args)
        self.code = code
        self.error = error
