from utils import get_limits
import cv2
from PIL import Image

yellow = [0,255,255] #yello in BGR colorspace
cap = cv2.VideoCapture(0) #which webcam to open
while True:
  ret, frame = cap.read() #take frame from the webcam

  hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert BGR image to HSV

  lowerLimit, upperLimit = get_limits(color= yellow) #get the regions of range

  mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)  #location of pixels we are interested

  mask_ = Image.fromarray(mask) #convert the info from numpy array to PIL form

  bbox = mask_.getbbox() #draw bounding box around yellow object

  if bbox is not None:
    x1, y1, x2, y2 = bbox

    #draw a rectangle bounding box with params :  frame, upper cordinate, lower cordinate, color of bbox, thickness
    cv2.rectangle(frame, (x1, y1), (x2,y2),(0,255,0), 5)
  print(bbox)

  cv2.imshow('frame', frame) #visualize the frame

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release() #release memory

cv2.destroyAllWindows()