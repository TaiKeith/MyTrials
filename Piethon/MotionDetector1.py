import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)  # Calculates diff btwn 1st frame and other frames
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations = 0)
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Define contour area/borders

    for contour in cnts:  # Removes noises and shadows
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Thresh", thresh_frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

cv2.destroyAllWindows()
