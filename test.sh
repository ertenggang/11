#!/bin/bash

m1=`base64 ./images/cat11.jpg`
m2=`base64 ./images/cat2.jpg`

curl -i --verbose -X POST  http://localhost:5000/image_match_api/?m1=${m1}\&m2=${m2}
