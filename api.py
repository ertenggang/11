from flask import Flask, request, jsonify
import urllib2
import cv2
import numpy as np

from image_match import image_match

app = Flask(__name__)

# @app.route('/', methods = ['GET', 'POST'])
# def hello_world():
#   if request.method == 'POST':
#     f = request.files['file']
#     f.save('./test.jpg')
#     return 'upload completed'
#   else:
#     return 'hello world'

def enum(**enums):
    return type('Enum', (), enums)

GET_IMAGE_STATUS = enum(EXCEPTION=1, FORMATERROR=2, OK=3)

def get_image(murl):
  try:
    req = urllib2.Request(murl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
    resp = urllib2.urlopen(req)
  except:
    return (GET_IMAGE_STATUS.EXCEPTION, None)
  m = resp.read()
  m = np.fromstring(m, np.uint8)
  m = cv2.imdecode(m, cv2.IMREAD_GRAYSCALE)
  if m is None:
    return (GET_IMAGE_STATUS.FORMATERROR, m)
  else:
    return  (GET_IMAGE_STATUS.OK, m)

@app.route('/image_match_api/', methods=['POST','GET'])
def image_match_api():
  param_num = 2
  error_info = []
  imgs = [[]]*param_num
  for i in range(param_num):
    url = request.values.get('m%d'%(i+1))
    (status, imgs[i]) = get_image(url)
    if status == GET_IMAGE_STATUS.EXCEPTION:
      error_info.append({'url':url, 'error': 'Exception raised during opening url.', 'info':'Invalid URL'})
    elif status == GET_IMAGE_STATUS.FORMATERROR:
      error_info.append({'url': url, 'error': 'Cannot decode image data', 'info':'Unsupported format or the access if refused.'})
    elif not status == GET_IMAGE_STATUS.OK:
      error_info.append({'url':url, 'error':'Unkown error.', 'info':''})

  if len(error_info) <= 0:
    [result, score, score_type, threshold] = image_match(imgs[0], imgs[1])
    return jsonify({'ret_code':0, 'result': {'match': result, 'score':score, 'score_type':score_type, 'threshold': threshold}})
  else:
    return jsonify({'error': 'Fail to fetch images.', 'error_info':error_info, 'ret_code':2101})


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')

