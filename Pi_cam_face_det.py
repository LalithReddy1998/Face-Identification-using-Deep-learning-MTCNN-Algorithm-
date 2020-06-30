import io
import picamera
import cv2
from mtcnn.mtcnn import MTCNN
import numpy
import time

detector = MTCNN()

for i in range(15):
    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.rotation = 180

        camera.capture(stream, format='jpeg')

        camera.resolution = (640, 480)
        print("capturing in 2 secs")
        # time.sleep(2)

        print("capture")

        buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
        image = cv2.imdecode(buff, 1)
        #image = cv2.flip(image, -1)
        #image = cv2.flip(image, +1)

        result = detector.detect_faces(image)

        for index, box in enumerate(result):
            bounding_box = box['box']
            cv2.rectangle(image,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2],
                           bounding_box[1] + bounding_box[3]),
                          (0, 155, 255),
                          2)
            x = bounding_box[0]
            y = bounding_box[1]
            h = bounding_box[3]
            w = bounding_box[2]
            crop = image[y:y+h, x:x+w].copy()
            cv2.imwrite(
                "/home/pi/Documents/mtcnn-master/py_facedetector/results/face"+str(index)+".jpeg", crop)
        cv2.imwrite('{0:01d}.jpeg'.format(i), image)
        print("Done")


print("result")
camera.stop_preview()

