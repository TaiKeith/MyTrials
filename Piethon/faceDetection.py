# Face Detection Using OpenCV

import cv2

# Create a CascadeClassifier Object
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cv2.data.haarcascades

# Reading the image as it is
img = cv2.imread("/home/tai/Downloads/Debugging-meme.png", 1)

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

#print(type(faces))
#print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

resized = cv2.resize(img, (int(img.shape[1]),int(img.shape[0])))

cv2.imshow("Gray", resized)

cv2.waitKey(0)

cv2.destroyllWindows()