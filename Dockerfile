FROM registry.cn-beijing.aliyuncs.com/zhuangwj/opencv:ubuntu14.04

MAINTAINER qianyelin "422036876@qq.com"

RUN mkdir /flask_app
WORKDIR /flask_app
RUN curl https://bootstrap.pypa.io/get-pip.py > get-pip.py && python get-pip.py && rm get-pip.py
RUN pip install flask
RUN git clone https://github.com/ertenggang/11.git .

CMD python api.py

EXPOSE 5000


