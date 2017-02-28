#!/bin/bash

# m1=`base64 ./images/cat11.jpg`
# m2=`base64 ./images/cat2.jpg`

m1=http://pic13.nipic.com/20110323/4768406_131856356184_2.jpg
m2=http://pic5.nipic.com/20100115/4128248_202946002093_2.jpg

curl -i --verbose -X POST  http://localhost:5000/image_match_api/?m1=${m1}\&m2=${m2}
