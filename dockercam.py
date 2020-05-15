# Script to test access to webcam  for opencv
# make sure the docker container started with -d /dev/vide0:/dev/video0
import numpy as np
import cv2

#access /dev/video0
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
