import cv2
import base64
import numpy as np

import feature_extractors
import feature_matchers

def image_match(m1, m2, threshold = 0.2):
  extrator = feature_extractors.local_features('ORB')
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

  return (result, match_score, score_type)

if __name__ == '__main__':
  m1 = cv2.imread('images/cat11.jpg')
  m2 = cv2.imread('images/cat12.jpg')
  m3 = cv2.imread('images/cat2.jpg')
  
  print image_match(m1, m2)
  print image_match(m1, m3)

