import cv2
import base64
import numpy as np

import feature_extractors
import feature_matchers

from image_match.goldberg import ImageSignature

def image_match(m1, m2, threshold = 0.2):
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

  return (result, match_score, score_type, threshold)

def image_duplication(m1, m2, threshold = 0.4):
  gis = ImageSignature()
  a = gis.generate_signature(m1, True)
  b = gis.generate_signature(m2, True)
  match_score = gis.normalized_distance(a, b)
  score_type = 'distance'
  result = match_score < threshold

  if result:
    result = 1
  else:
    result = 0

  return (result, match_score, score_type, threshold)


if __name__ == '__main__':
  m1 = cv2.imread('images/cat11.jpg')
  m2 = cv2.imread('images/cat12.jpg')
  m3 = cv2.imread('images/cat2.jpg')
  
  # print image_match(m1, m2)
  # print image_match(m1, m3)
  print image_duplication(m1, m2)




