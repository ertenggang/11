from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np

from image_match import image_match

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    f = request.files['file']
    f.save('./test.jpg')
    return 'upload completed'
  else:
    return 'hello world'


@app.route('/image_match_api/', methods=['POST','GET'])
def image_match_api():
  m1 = request.args.get('m1')
  m2 = request.args.get('m2')

  try:
    m1 = m1.replace(' ','+')
    m1 = base64.decodestring(m1)
    m2 = m2.replace(' ','+')
    m2 = base64.decodestring(m2)
  except:
    return jsonify({'error': 500001, 'info':'invalid base64 code!'})


  m1 = np.fromstring(m1, np.uint8)
  m1 = cv2.imdecode(m1, cv2.IMREAD_GRAYSCALE)
  m2 = np.fromstring(m2, np.uint8)
  m2 = cv2.imdecode(m2, cv2.IMREAD_GRAYSCALE)

  [result, score, score_type] = image_match(m1, m2)
  return jsonify({'result': result, 'score':score, 'score_type':score_type})
  # return jsonify({'m1base64': m1})
