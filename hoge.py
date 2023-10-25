import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import time 
start = time.time()
from ultralytics import YOLO
print("import_time:",time.time()-start)

start = time.time()
mode = YOLO("./runs/detect/train2/weights/best.pt")
print("mode_time:",time.time()-start)
# start = time.time()
# cap = cv2.VideoCapture(0) 
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
# print("cap_time:",time.time()-start)
# ret ,frame = cap.read()
# print("read_time:",time.time()-start)
# while True:
#     # ret, frame = cap.read()
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break