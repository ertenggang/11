import feature_extractors
import feature_matchers

def image_match(m1, m2, threshold = 200):
  extrator = feature_extractors.local_features('SIFT')
  matcher = feature_matchers.local_features_matcher('RANSAC')

  fea1 = extrator.feature_extract(m1)
  fea2 = extrator.feature_extract(m2)

  match_score = matcher.match(fea1, fea1)
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

