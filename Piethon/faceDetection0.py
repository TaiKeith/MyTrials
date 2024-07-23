import cv2

# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("/home/tai/Downloads/Debugging-meme.png", 1)

resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)))

cv2.imshow("Liam", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
