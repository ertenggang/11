import cv2

class local_features():
  def __init__(self, feature_type='ORB'):
    self.feature_type = feature_type
    self.max_edge = 500
    # self.extractor = getattr(cv2.xfeatures2d, self.feature_type+'_create')()
    self.extractor = getattr(cv2, self.feature_type+'_create')()

  def feature_extract(self, im):
    height, width = im.shape[:2]
    if len(im.shape) >= 3 and im.shape[-1] >=4:
      im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    max_edge = max(height, width)
    scale = float(self.max_edge)/max_edge

    if scale < 1:
      im = cv2.resize(im,(int(scale*width), int(scale*height)))
    kp, dep = self.extractor.detectAndCompute(im, None)

    kp_positions = []
    for k in kp:
      kp_p = k.pt
      kp_positions.append(kp_p)


    fea = dict({'kp':kp_positions, 'dep':dep , 'size':im.shape[:2]})
    return fea

     
