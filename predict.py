from Mask_RCNN.mrcnn.model import mold_image
from Mask_RCNN.mrcnn.config import Config
from Mask_RCNN.mrcnn.model import MaskRCNN
from numpy import expand_dims
import cv2
import time

# define the prediction configuration
class PredictionConfig(Config):
	# define the name of the configuration
	NAME = "head_cfg"
	# number of classes (background + head)
	NUM_CLASSES = 1 + 1
	# simplify GPU config
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1

#load model
cfg = PredictionConfig()
# define the model
model = MaskRCNN(mode='inference', model_dir='./', config=cfg)
# load model weights
model.load_weights('model.h5', by_name=True)

# load image
image = cv2.imread("2.jpg")
start_time = time.time()
# convert pixel values (e.g. center)
scaled_image = mold_image(image, cfg)
# convert image into one sample
sample = expand_dims(scaled_image, 0)
# make prediction
yhat = model.detect(sample, verbose=0)
print("--- %s seconds ---" % (time.time() - start_time))
print(yhat)
for box in yhat[0]['rois']:
	# get coordinates
	y1, x1, y2, x2 = box
	# calculate width and height of the box
	cv2.rectangle(image, (x1, y1), (x2, y2), (255,0,0), 1)
cv2.imshow("Head detection", image)
cv2.waitKey(0)