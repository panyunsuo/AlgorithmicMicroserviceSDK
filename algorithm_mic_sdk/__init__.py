"""
安装
pip install leqi-algorithm-mic-sdk

算法模块
algorithm_mic_sdk.error 异常模块
algorithm_mic_sdk.error.AbnormalAlgorithmPlatform API网关相关异常
algorithm_mic_sdk.auth.AuthInfo 账号信息,需要初始化后作为参数给其他需要验证的模块调用

algorithm_mic_sdk.base 基础类库模块
algorithm_mic_sdk.base.Base 主要是对图片算法的处理,可以上传/下载图片, 获取算法结果等,详细使用见模块说明
algorithm_mic_sdk.base.AlgoBase 对Base模块的封装,主要是有同步/异步发布算法的功能

algorithm_mic_sdk.algorithms.topic.Topic 错题本算法
algorithm_mic_sdk.algorithms.trace_elimination.TraceElimination 手写痕迹消除算法
"""
__version__ = '1.24.1'
