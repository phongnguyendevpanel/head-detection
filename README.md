# head-detection
## A. Model file: https://robber-detection.s3-ap-southeast-1.amazonaws.com/Head-Detection-App/model.h5

## B. Mask-RCNN package: https://robber-detection.s3-ap-southeast-1.amazonaws.com/Head-Detection-App/mask_rcnn.tar.gz
### 1. Extract Mask-RCNN file. Put it and the model file in the working directory

## C. Create a folder named "images" in the working directory and put images you want to test in it.
### 1. Example: python predict.py --path photo.jpg
### 2. There will be a .jpg file created in the "images" folder, and it is the result.
