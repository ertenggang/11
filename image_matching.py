import cv2
import base64
import numpy as np

import feature_extractors
import feature_matchers

from image_match.goldberg import ImageSignature

def img_decode_cv(img):
  img = np.fromstring(img, np.uint8)
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  return img

def image_match(m1, m2, threshold = 0.2):
  result = 0
  match_score = 0
  score_type = ''
  info = {}

  m1 = img_decode_cv(m1)
  if m1 is None:
    info['m1'] = 'Invalid image data!'
  m2 = img_decode_cv(m2)
  if m2 is None:
    info['m2'] = 'Invalid image data!' 

  if len(info) == 0:
    extrator = feature_extractors.local_features('SIFT')
    matcher = feature_matchers.local_features_matcher('RANSAC')

    fea1 = extrator.feature_extract(m1)
    fea2 = extrator.feature_extract(m2)

    match_score = matcher.match(fea1, fea2)
    score_type = matcher.flag

    if score_type == 'distance':
      result = match_score < threshold
    else:
      result = match_score > threshold

    if result:
      result = 1
    else:
      result = 0

  return (result, match_score, score_type, threshold, info)

def image_duplication(m1, m2, threshold = 0.4):
  result = 0
  match_score = 0
  score_type = ''
  info = {}

  gis = ImageSignature()
  try:
    a = gis.generate_signature(m1, True)
  except:
    info['m1'] = 'Invalid image data!'
  try:
    b = gis.generate_signature(m2, True)
  except:
    info['m2'] = 'Invalid image data!'

  if len(info) == 0:
    match_score = gis.normalized_distance(a, b)
    score_type = 'distance'
    result = match_score < threshold

    if result:
      result = 1
    else:
      result = 0

  return (result, match_score, score_type, threshold, info)


if __name__ == '__main__':
  m1 = cv2.imread('images/cat11.jpg')
  m2 = cv2.imread('images/cat12.jpg')
  m3 = cv2.imread('images/cat2.jpg')
  
  # print image_match(m1, m2)
  # print image_match(m1, m3)
  print image_duplication(m1, m2)




