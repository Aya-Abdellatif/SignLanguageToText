

import cv2 as cv
import time
import os
import uuid

ImagesPath=""

labels=['peace','hello','yes','no','callme','highfive','dislike','goodjob','iloveyou']
imgnums=20

for label in labels:
  cap=cv.VideoCapture(0)
  print(f"{label}")
  time.sleep(5)
  for imgnum in range(imgnums):
    ret,frame=cap.read()
    imagename=os.path.join(ImagesPath,label,str(imgnum)+'.jpg')
    cv.imwrite(imagename,frame);
    cv.imshow('frame',frame);
    time.sleep(2);
    if cv.waitKey(1) and 0xFF ==ord('q'):
      break;
  cap.release()