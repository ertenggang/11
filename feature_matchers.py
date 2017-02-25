import cv2
import numpy as np

class local_features_matcher():
  def __init__(self, match_method='RANSAC'):
    self.flag = 'distance'
    self.match_method = getattr(cv2, match_method)
    self.rej_threshold = 1
    self.max_iter= 1000
    self.confidence = 0.99


  def match(self, qfea, gfea):
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(qfea['dep'], gfea['dep'])

    srcpoints = []
    dstpoints = []
    for m in matches:
      srcpoints.append(qfea['kp'][m.queryIdx])
      dstpoints.append(gfea['kp'][m.trainIdx])

    srcpoints = np.array(srcpoints)
    dstpoints = np.array(dstpoints)

    transform = cv2.findHomography(srcpoints, dstpoints, self.match_method, self.rej_threshold)[0]
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
      error = np.mean(np.sqrt(np.sum(diff*diff,1)))
      return error




