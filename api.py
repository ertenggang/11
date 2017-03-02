from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np

from image_match import image_match

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    return 'hello world'


@app.route('/image_match_api/', methods=['POST','GET'])
def image_match_api():
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
  
  for i in range(param_num):
    imgs[i] = np.fromstring(imgs[i], np.uint8)
    imgs[i] = cv2.imdecode(imgs[i], cv2.IMREAD_GRAYSCALE)
    if imgs[i] is None:
      info[param_name] = 'Invalid image data!'
  if len(info) > 0:
    return jsonify({'ret_code':2101, 'error':'Invalid data.', 'detail':info})


  [match, score, score_type, threshold] = image_match(imgs[0], imgs[1])
  return jsonify({'ret_code':0, 'result':{'match':match, 'score':score, 'score_type':score_type, 'threshold':threshold}})

  



  # m1 = request.values.get('m1')
  # m2 = request.values.get('m2')

  # try:
  #   m1 = m1.replace(' ','+')
  #   m1 = base64.decodestring(m1)
  #   m2 = m2.replace(' ','+')
  #   m2 = base64.decodestring(m2)
  # except:
  #   return jsonify({'error': 2101, 'info':'invalid base64 code!'})

  # m1 = np.fromstring(m1, np.uint8)
  # m1 = cv2.imdecode(m1, cv2.IMREAD_GRAYSCALE)
  # m2 = np.fromstring(m2, np.uint8)
  # m2 = cv2.imdecode(m2, cv2.IMREAD_GRAYSCALE)

  # if m1 is None or m2 is None:
  #   check_parmas = []
  #   if 

  # [result, score, score_type] = image_match(m1, m2)
  # return jsonify({'result': result, 'score':score, 'score_type':score_type})
  # # return jsonify({'m1base64': m1})


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
  
