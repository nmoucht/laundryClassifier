import cv2
from argparse import ArgumentParser

import sys
filename = sys.argv[1:][0]
sizeWidth =  sys.argv[1:][1]
sizeHeight =  sys.argv[1:][2]
# print(sizeWidth)
# print(sizeHeight)
image = cv2.imread(filename)
resized_image = cv2.resize(image, (int(sizeHeight), int(sizeWidth)))
cv2.imwrite("resized.jpg", resized_image)