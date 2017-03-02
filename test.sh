#!/bin/bash

# m1=`base64 ./images/cat11.jpg`
# m2=`base64 ./images/cat2.jpg`

hosturl=http://localhost:5000/

m1=ad # 参数不是url
m2=http://www.cvcraft.cn/ #url不能访问
curl -i --verbose -X POST  ${hosturl}image_match_api/?m1=${m1}\&m2=${m2}

m1=www.baidu.com # 参数url指向的不是图片
m2=http://i.dimg.cc/e2/18/43/58/e8/51/e5/d3/ad/2d/b5/7d/06/36/2a/ef.jpg
curl -i --verbose -X POST  ${hosturl}image_match_api/?m1=${m1}\&m2=${m2}

# 图片能够正常解码
# 不同图片
m1=http://i.dimg.cc/e2/18/43/58/e8/51/e5/d3/ad/2d/b5/7d/06/36/2a/ef.jpg
m2=http://pic5.nipic.com/20100115/4128248_202946002093_2.jpg
curl -i --verbose -X POST  ${hosturl}image_match_api/?m1=${m1}\&m2=${m2}

# 相同图片
m1=http://img.zjol.com.cn/pic/0/04/73/48/4734835_790056.jpg
m2=http://img.zcool.cn/community/0124085724667032f875a399b3f1d8.jpg
curl -i --verbose -X POST  ${hosturl}image_match_api/?m1=${m1}\&m2=${m2}
