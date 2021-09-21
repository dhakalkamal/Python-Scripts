import hdf5storage
import os 
import cv2
from PIL import Image
import PIL
import numpy as np
from imutils import paths
from tifffile import imsave
data_dir = os.path.join("video1.mat")
data = hdf5storage.loadmat(data_dir)
#print(data)
data_image = data['depthFrameData']
print(data_image.dtype)
PATH = "depthframes/depth{0000}.jpg"
imageid = 0
for i in range(300):
    image = data_image[:,:, i:i+1]
    image = image/image.max()
    image = image.astype(np.float64)
    print(image.dtype)
    print(image.shape[:3])
    #image = image.astype(np.uint8)
    #image = cv2.imread(image)
    #image = Image.open
    #image = (image/256).astype(np.uint8)
    #print(image[1])
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    cv2.imshow("Image", image)
    #cv2.imwrite("savedimage1.png", image )
    cv2.imwrite(PATH.format(imageid), image*255)
    #cv2.imwrite("frame%d.jpg" %imageid, image)
    #imsave(PATH.format(imageid), image)
    imageid += 1
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

#for i in range(300):
#    cv2.imshow("Frame", data_image[i:])

#frint
#data_image= data_image[:2]
# image= Image.fromarray(data_image)
#PIL.Image.save(image)
#im = Image(data_image)
#im.open()
#print(data_image[1][:0:1]) 

#image = Image(data_image)
#print(image)
'''
cap = cv2.VideoCapture('data')
#cap = cv2.VideoCapture('data_image')
while True:
    ret, frame = cap.read()
    cv2.imshow("image", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()

#print(data_image)
'''