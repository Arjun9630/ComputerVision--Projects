import cv2
import mediapipe as mp

mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
webcam = cv2.VideoCapture(0)

while True:    #Real-time webcam feed!
    ret, frame = webcam.read()
    if not ret:
        break

    H, W, _ = frame.shape
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #Converts the frame to RGB colorspace
    results = faceDetection.process(imgRGB) #Mediapipe detects for face in the frame!

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box  #Relative location to fit any resolution
            x1, y1, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H) #Frame specific dimensions
            frame[y1:y1 + h, x1:x1 + w] = cv2.blur(frame[y1:y1 + h, x1:x1 + w], (50, 50))  # Apply blur to face region

    cv2.imshow("img", frame)
    if cv2.waitKey(1) == ord('q'):   #stop displaying when 'q' is given as the input
        break

webcam.release()
cv2.destroyAllWindows()















