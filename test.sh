#!/bin/bash

# m1=`base64 ./images/cat11.jpg`
# m2=`base64 ./images/cat2.jpg`

m1=http://i.dimg.cc/e2/18/43/58/e8/51/e5/d3/ad/2d/b5/7d/06/36/2a/ef.jpg
m2=http://pic5.nipic.com/20100115/4128248_202946002093_2.jpg
# m1=http://www.cvcraft.cn/
# m2=h

curl -i --verbose -X POST  http://localhost:5000/image_match_api/?m1=${m1}\&m2=${m2}
