# 打包发布教程

## 1. 注册账号
到[https://pypi.org/](https://pypi.org/)网站去注册账号

## 2. 配置`.pypirc`文件
> 对于`mac/linux`,添加`~/.pypirc`文件
> 对于`win`系统,添加`C:/Users/<name>/.pypirc`文件

* 文件内容:
```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = name # 账号名
password = password # 密码 
```

## 3. 安装`twine`
`pip install twine -i https://mirrors.aliyun.com/pypi/simple/`

## 4. 添加`MANIFEST.in`文件
如果不在`MANIFEST.in`文件中添加一些项目安装所需的文件,那么在安装时可能会报`FileNotFoundError`错误

* 例如,项目的`setup.py`中需要读取`readme.md`文件,那么就需要在`MANIFEST.in`文件中添加:`include readme.md` 或者`include *.md`

## 分包
将项目按版本号打包`python setup.py sdist`

## 上传
`twine upload dist/*`

