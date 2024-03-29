# 安装  
`pip install leqi-algorithm-mic-sdk`

# 算法模块

* `algorithm_mic_sdk.error` 异常模块  
* * `algorithm_mic_sdk.error.AbnormalAlgorithmPlatform` API网关相关异常  
* `algorithm_mic_sdk.auth.AuthInfo` 账号信息,需要初始化后作为参数给其他需要验证的模块调用  
* `algorithm_mic_sdk.base` 基础类库模块
* * `algorithm_mic_sdk.base.Base` 主要是对图片算法的处理,可以上传/下载图片, 获取算法结果等,详细使用见模块说明
* * `algorithm_mic_sdk.base.AlgoBase` 对`Base`模块的封装,主要是有同步/异步发布算法的功能

* `algorithm_mic_sdk.algorithms.topic.Topic` 错题本算法
* `algorithm_mic_sdk.algorithms.trace_elimination.TraceElimination` 手写痕迹消除算法
* `algorithm_mic_sdk.algorithms.speech_recognition_chinese.SpeechRecognitionChinese` 中文语音识别算法
* `algorithm_mic_sdk.algorithms.speech_recognition_english.SpeechRecognitionEnglish` 英文语音识别算法
* `algorithm_mic_sdk.algorithms.fluorescent_pen_recognition.FluorescentPenRecognition` 荧光笔识别算法
* `algorithm_mic_sdk.algorithms.region_marquee.RegionMarquee` 错题本框题算法
* `algorithm_mic_sdk.algorithms.photo_to_cartoon.PhotoToCartoon` 人像转卡通头像算法
* `algorithm_mic_sdk.algorithms.skin_recognition.SkinRecognition` 皮肤病检测算法
* `algorithm_mic_sdk.algorithms.watermark_removal.WatermarkRemoval` 去水印算法
* `algorithm_mic_sdk.algorithms.ocr_rec.OCRRec` 图片文本检测算法
* `algorithm_mic_sdk.algorithms.paper_rotation.PaperRotation` 错题本图像旋转算法
* `algorithm_mic_sdk.algorithms.speech_synthesis.SpeechSynthesis` 语音合成算法
* `algorithm_mic_sdk.algorithms.topic_loc.TopicLoc` 错题本题干检测定位算法
* `algorithm_mic_sdk.algorithms.teacher_qualification_check.TeacherQualificationCheck` 教师资格证编号识别算法

* `algorithm_mic_sdk.ws.speech_recognition_chinese.SpeechRecognitionChinese` 中文识别算法(socket 版本)
* `algorithm_mic_sdk.ws.speech_recognition_english.SpeechRecognitionEnglish` 英文识别算法(socket 版本)


# 使用示例1 (http api):

> 错题本算法


```python

import time

from algorithm_mic_sdk import error
from algorithm_mic_sdk.algorithms.topic import Topic
from algorithm_mic_sdk.auth import AuthInfo
from algorithm_mic_sdk.base import Base
from algorithm_mic_sdk.tools import FileInfo

auth_info = AuthInfo(host='http://gateway.algo.leqi.us', user_name='your name', password='your password')

# 需要处理的文件
filename = '1.jpg'

# 构建FileInfo对象
# 对于需要上传文件的地方,都可以通过直接初始化FileInfo对象来实现文件的自动上传.
# FileInfo内支持从二进制/文件url/OSS存储名(leqi-algo下)/可执行方法中获得文件信息
# 具体使用方法见FileInfo类说明
file_info = FileInfo.for_file_bytes(open(filename, 'rb').read())

# corners参数
corners = [[0, 0], [2160, 0], [0, 3840], [2160, 3840]]

# 创建算法对象,各个算法的各个参数具体含义可见文档
topic = Topic(auth_info=auth_info, file=file_info, corners=corners)

# 同步请求算法(会阻塞至算法处理完成后返回)
resp = topic.synchronous_request()
print('同步请求算法完成', resp.json, '\n')

# 异步发布任务(需要轮询获取任务处理结果)
resp = topic.asynchronous_request()
print('异步发布任务得到任务ID为', resp.task_id, '\n')

# 根据任务ID获取处理结果
try:
    # 使用Base类来操作任务结果
    base = Base(auth_info=auth_info)
    while True:
        resp = base.get_results(resp.task_id)
        if resp.gateway_code == 1001:
            # 算法处理失败
            print('算法处理失败', resp.error)
        elif resp.gateway_code == 1002:
            # 任务仍然在处理中,休眠1s后继续请求
            time.sleep(1)
            continue
        elif resp.gateway_code != 1000:
            # 其他状态码
            print('算法未知状态码 ', resp.gateway_code, resp.gateway_error)
            break

        # resp.gateway_code==1000时,则表明算法处理完成,但不代表算法处理成功
        # 判断算法服务器状态码,若该图片无法处理之类的提示可在此判断
        if resp.code != 200:
            print('算法制作异常 code:', resp.code, 'message', resp.message)
            break

        # 从返回值中拿到结果图,各个算法的返回参数可见文档
        result_im_oss_name = resp.result['result_im_oss_name']

        # 生成图片预览的url(可以视情况加水印,此处的url由于是给外网访问的,所以extranet参数要为True)
        url = base.get_file_url(result_im_oss_name, extranet=True)
        print('url', url)

        # 下载文件到本地
        img_bytes = base.get_file(oss_name=result_im_oss_name)
        with open('beauty_file.png', 'wb') as f:
            f.write(img_bytes)
        print('文件下载成功 ./beauty_file.png')
        break

except error.AbnormalAlgorithmPlatform as e:
    # 算法平台对除未制作完成的异常外进行全异常捕捉
    print('算法平台异常 状态码:', e.code, '状态提示', e.error)
except Exception as e:
    print('未知异常 ', e)

```

# 使用示例2 (websocket api):
> 中文语音识别算法

```python
from algorithm_mic_sdk.auth import AuthInfo
from algorithm_mic_sdk.ws.speech_recognition_chinese import SpeechRecognitionChinese

host = 'ws://gateway.algo.leqi.us:8005'  # 算法host地址,协议头为ws
user_name = 'your name'
password = 'password'
filename = '1.pcm' # 音频文件名,这里采用文件的方式来模拟读取流数据,在实际场景中,这个数据可能是由客户端与服务器的socket连接句柄中读取
audio_format = 'PCM' # 音频格式


def callback(ws, data):
    # 回调函数 入参两个参数,一个是当前连接句柄,一个是识别的结果,这里只是对识别结果做简单输出
    print(data)

# 创建一个获取流数据的迭代器,在实际场景中,这个数据可能是由客户端与服务器的socket连接句柄中读取
def send_request_body(stream_filename):
    data = open(stream_filename, 'rb').read()
    while data:
        d, data = data[:320], data[320:]
        yield d
# 初始化权限信息类
auth_info = AuthInfo(host=host, user_name=user_name, password=password)
# 创建一个识别句柄
speech_recognition_chinese = SpeechRecognitionChinese(auth_info, audio_format, send_request_body(filename), callback)
# 运行请求算法,执行此步骤将会发生阻塞
speech_recognition_chinese.run()
``` 