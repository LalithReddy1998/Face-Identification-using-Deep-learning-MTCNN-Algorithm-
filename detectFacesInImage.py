import io
import picamera
import cv2
from mtcnn.mtcnn import MTCNN
import numpy
import time


detector = MTCNN()

image = cv2.imread('group.jpg')


print("before")
result = detector.detect_faces(image)
print("after")
for index,box in enumerate(result):
    bounding_box = box['box']
    cv2.rectangle(image,
                (bounding_box[0], bounding_box[1]),
                (bounding_box[0]+bounding_box[2], bounding_box[1] +   bounding_box[3]),
                (0,155,255),
                2)
    x = bounding_box[0]
    y = bounding_box[1]
    h = bounding_box[3]
    w = bounding_box[2]
    crop=image[y:y+h,x:x+w].copy()
    cv2.imwrite("/home/pi/Documents/mtcnn-master/py_facedetector/results/face"+str(index)+".jpeg", crop)
cv2.imwrite("output.jpg",image )
print("Done")
    
print(result)

