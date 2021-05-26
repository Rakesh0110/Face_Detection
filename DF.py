#import required libraries
import cv2
import numpy as np
import dlib
#connect to your webcam
cap=cv2.VideoCapture(0)
#detect the coordinates
detector=dlib.get_frontal_face_detector()
#capture frame continously
while True:
  ret,frame=cap.read()
  frame=cv2.flip(frame,1)
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces=detector(gray)
  i=0
#counting no of faces
  for face in faces:
    #get the cordinates of faces
    x,y=face.left(),face.top()
    x1,y1=face.right(),face.bottom()
    cv2.rectangle(frame,(x,y),(x1,y1),(0,255,0),2)
    #increment for each faces
    i=i+1
    #display the box and faces
    cv2.putText(frame,'Face_'+str(i),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    print(face,i)
  #display the resulting frame
  cv2.imshow('frame', frame)
  #press q button to quit
  if cv2.waitKey(1)& 0xFF==ord('q'):
    break
#release the capture nd destroy windows
cap.release()
cv2.destroyAllWindows()