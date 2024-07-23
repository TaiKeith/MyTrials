import cv2, time

video = cv2.VideoCapture(0)  # Create a VideoCapture object to record video using webcam

a = 1

while True:
    a += 1
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame color to greyscale

    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

print(a)  # This will print the number of frames

video.release()

cv2.destroyAllWindows()
