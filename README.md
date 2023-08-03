# Face-Identification-using-Deep-learning-MTCNN-Algorithm-
This project is face identification project the algorithm which i have used is MTCNN Algorithm where it gives more accuracy.

I successfully spearheaded an Automated Attendance Management System project using Deep Learning. I initially employed machine learning techniques to discern case files, albeit with limited success. However, I transitioned to the highly effective MTCNN deep learning algorithm. This solution initially identifies faces within images, cropping and cataloging them in a dedicated folder for subsequent identification.

To streamline operations, I transposed the entire Python-based code onto an IoT Raspberry Pi platform. For facial recognition, I harnessed the capabilities of AWS. This involved transmitting cropped images to an S3 bucket, which subsequently relayed them to AWS Recognition Services. Through this workflow, attendance records were meticulously logged.

To automate the entire process, I developed a series of bash scripts. This orchestrated system substantially enhanced efficiency and accuracy across the attendance management process.


There are two different codes :
1)detectFacesInImage
       This peace of code will identify the faces in image where the input is image.jpeg
       
2)Pi_cam_face_det:
       This can be used with picam raspberrypi devise where it uses live camera and take photoes and detect face.
