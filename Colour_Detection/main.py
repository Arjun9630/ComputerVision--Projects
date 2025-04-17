import cv2
import utils
from PIL import Image

webcam = cv2.VideoCapture(0)
yellow = [0,255,255]  # Target color in BGR (approximate yellow)

while True:
    ret, frame = webcam.read()
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #Converts the frame to HSV colorspace

    lowerLimit, upperLimit = utils.get_limits(yellow) #to get lower and upper limit

    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit) # Create a binary mask where target color pixels are white and others are black

    mask_ = Image.fromarray(mask) #Secondary mask to draw bounding box
    boundingBox = mask_.getbbox()

    if boundingBox is not None:
        x1, y1, x2, y2 = boundingBox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) #Drawing rectangle using cv2 function

    cv2.imshow("Realtime Webcam Feed", cv2.resize(frame, (955,540)))

    if cv2.waitKey(1) == ord('q'): #stop displaying when 'q' is given as the input
        break

webcam.release()
cv2.destroyAllWindows()
