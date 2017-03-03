FROM docker pull registry-internal.cn-qingdao.aliyuncs.com/zhuangwj/image-env:latest

MAINTAINER qianyelin "422036876@qq.com"

RUN mkdir /flask_app
WORKDIR /flask_app
RUN git clone https://github.com/ertenggang/11.git .

CMD python api.py

EXPOSE 5000


