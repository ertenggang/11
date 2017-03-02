FROM registry.cn-beijing.aliyuncs.com/zhuangwj/opencv:ubuntu14.04

MAINTAINER qianyelin "422036876@qq.com"

RUN mkdir /flask_app
WORKDIR /flask_app
RUN git clone https://github.com/ertenggang/11.git .
RUN python get-pip.py && rm get-pip.py
RUN pip install flask


CMD python api.py

EXPOSE 5000


