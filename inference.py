import cv2 as cv
import keras
import numpy as np
import mediapipe as mp
import tensorflow as tf


model = keras.models.load_model('SignLanguage9C991.h5')
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()



cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 500)

CATEGORIES = ["hello", "yes", "no", "iloveyou", "callme", "goodjob", "highfive", "dislike", "peace"]


def get_zero_hand():
  return [[0, 0, 0]] * 21

def get_landmark_array(landmarks):
  arr = []
  for l in landmarks:
    arr.append([l.x, l.y, l.z])
  return np.array(arr)


def get_rectange(landmarks, h, w):
    x_max, y_max, x_min, y_min = 0, 0, w, h
    for lm in landmarks:
        x, y = int(lm.x * w), int(lm.y * h)
        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x
        if y > y_max:
            y_max = y
        if y < y_min:
            y_min = y
    return x_min, y_min, x_max, y_max


def predict(img, draw_rectangle=True):
  imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
  result = hands.process(imgRGB)
  if result.multi_hand_landmarks:

    for hand in result.multi_hand_landmarks:
      x_min, y_min, x_max, y_max = None, None, None, None
      # Drawing Rectangle
      if draw_rectangle:
        h, w, c = img.shape
        x_min, y_min, x_max, y_max = get_rectange(hand.landmark, h, w)
        cv.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)


      # Predicting
      data = get_landmark_array(hand.landmark)
      data = data.reshape((1, 21, 3))
      result = model.predict(data)

      if draw_rectangle:
          cv.putText(img, f"{CATEGORIES[result.argmax()]}, {int(max(result[0]) * 100)}%" , (x_min, y_min), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
      
      break # Delete Break if you want to detect more than one hand
    return True
  else:
    return False


while True:
    success, frame = cap.read()
    predict(frame)


    cv.imshow("Video", frame)
    cv.waitKey(1)


