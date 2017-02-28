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

def get_image(murl):
  req = urllib2.Request(murl)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
  resp = urllib2.urlopen(req)
  m = resp.read()
  m = np.fromstring(m, np.uint8)
  m = cv2.imdecode(m, cv2.IMREAD_GRAYSCALE)
  return m

@app.route('/image_match_api/', methods=['POST','GET'])
def image_match_api():
  m1_url = request.args.get('m1')
  m2_url = request.args.get('m2')

  m1 = get_image(m1_url)
  m2 = get_image(m2_url)

  if m1 is None or m2 is None:
    check_params = {}
    if m1 is None:
      check_params['m1'] = m1_url
    if m2 is None:
      check_params['m2'] = m2_url
    return jsonify({'error': 'Fail to fetch images.', 'error_info':{'suggest':'The url of image is invaluable or the format of image is not supported.', 'check_params':check_params}, 'error_code':2101})

  [result, score, score_type] = image_match(m1, m2)
  return jsonify({'result': result, 'score':score, 'score_type':score_type})


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')

