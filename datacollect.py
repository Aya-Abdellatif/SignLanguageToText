import cv2 as cv
import time
import os

ImagesPath = os.path.join(os.getcwd(), 'data')

labels = ['peace','hello','yes','no','callme','highfive','dislike','goodjob','iloveyou']
imgnums = 20

for label in labels:
  cap = cv.VideoCapture(0)
  print(f"{label}")
  time.sleep(5)
  for imgnum in range(imgnums):
    ret, frame=cap.read()

    if not os.path.exists(os.path.join(ImagesPath, label)):
      os.mkdir(os.path.join(ImagesPath, label))

    imagename = os.path.join(ImagesPath, label, str(imgnum) + '.jpg')
    cv.imwrite(imagename, frame)
    cv.imshow('frame', frame)
    time.sleep(2)
    if cv.waitKey(1) and 0xFF ==ord('q'):
      break
  cap.release()