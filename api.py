from flask import Flask, request, jsonify
import urllib2
import base64
import numpy as np
import cv2

from image_matching import image_match
from image_matching import image_duplication

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    return 'hello world'


@app.route('/image_match_api/<level>', methods=['POST','GET'])
def image_match_api(level):
  param_num = 2
  imgs = [[]]*param_num
  info = {}
  
  for i in range(param_num):
    param_name = 'm%s'%(i+1)
    imgs[i] = request.values.get(param_name) 
    try:
      imgs[i] = imgs[i].replace(' ', '+')
      imgs[i] = base64.decodestring(imgs[i])
    except:
      info[param_name] = 'Invalid base64 code!'

  if len(info) > 0:
    return jsonify({'ret_code':2101, 'error':'Invalid data.', 'detail':info})

  if level == 'match':
    [match, score, score_type, threshold, info] = image_match(imgs[0], imgs[1])
  elif level == 'duplication':
    print type(imgs[0])
    [match, score, score_type, threshold, info] = image_duplication(imgs[0], imgs[1])
  else:
    pass
  
  if len(info) > 0:
    return jsonify({'ret_code':2101, 'error':'Invalid data.', 'detail':info})
  return jsonify({'ret_code':0, 'result':{'match':match, 'score':score, 'score_type':score_type, 'threshold':threshold}})



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')

