import cv2
import numpy as np

class local_features_matcher():
  def __init__(self, match_method='RANSAC'):
    self.flag = 'distance'
    self.match_method = getattr(cv2, match_method)
    self.rej_threshold = 5
    self.max_iter= 1000
    self.confidence = 0.99


  def match(self, qfea, gfea):
    # bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(qfea['dep'], gfea['dep'], k=2)

    # FLANN_INDEX_KDTREE = 0
    # index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees = 5)
    # search_params = dict(checks=50)

    # flann = cv2.FlannBasedMatcher(index_params, search_params)

    # matches = flann.knnMatch(qfea['dep'], gfea['dep'], k=2)

    good_matches = []
    for m, n in matches:
      if m.distance < 0.75*n.distance:
        good_matches.append(m)

    srcpoints = []
    dstpoints = []
    for m in good_matches:
      srcpoints.append(qfea['kp'][m.queryIdx])
      dstpoints.append(gfea['kp'][m.trainIdx])

    srcpoints = np.array(srcpoints)
    dstpoints = np.array(dstpoints)

    transform = cv2.findHomography(srcpoints, dstpoints, self.match_method, self.rej_threshold, maxIters=self.max_iter, confidence=self.confidence)[0]
    if transform is None:
      return float("inf")
    else:
      s = qfea['size']
      srcpoints = np.array([[0,0], [0, s[0]], [s[1], 0], [s[1], s[0]]])
      s = gfea['size']
      dstpoints = np.array([[0,0], [0, s[0]], [s[1], 0], [s[1], s[0]]])

      ori_points = np.c_[srcpoints, np.ones(srcpoints.shape[0])].T
      c = np.dot(transform, ori_points)
      c = c.T[:,:-1]
      diff = c-dstpoints
      error = np.mean(np.sqrt(np.sum(diff*diff,1)))/sum(gfea['size'])
      return error




