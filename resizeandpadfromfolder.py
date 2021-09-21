import cv2
import numpy as np
from imutils import paths
import argparse
import imutils

# construct the argument parser to aprse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, 
				help = "path to the dataset folder containing images")
args = vars(ap.parse_args())

PATH = "personbucketyolo/personbucket{00000}.png"
def resizeAndPad(img, size, padColor=0):

    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
        pad_horz = (sw-new_w)/2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    else: # square image
        new_h, new_w = sh, sw
        pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0

    # set pad color
    if len(img.shape) is 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)

    return scaled_img

#v_img = cv2.imread('oktest3.jpg') # vertical image
#scaled_v_img = resizeAndPad(v_img, (200,200), 127)
ImageId = 0
for (i, imagePath) in enumerate(paths.list_images(args["dataset"])):
	#h_img = cv2.imread('bucket.png') # horizontal image
	h_img = cv2.imread(imagePath)
	scaled_h_img = resizeAndPad(h_img, (1280,1280), 0)
	#cv2.imshow("resizedandpadimg", scaled_h_img)
	#cv2.imwrite("resized_bucket_newpad.png", scaled_h_img)
	cv2.imwrite(PATH.format(ImageId), scaled_h_img)
	ImageId += 1
	
cv2.waitKey(0)
#sq_img = cv2.imread('sq.jpg') # square image
#scaled_sq_img = resizeAndPad(sq_img, (200,200), 127)
