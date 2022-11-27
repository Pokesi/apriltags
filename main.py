from pupil_apriltags import Detector

import numpy as np
import cv2 as cv

at_detector = Detector(
   families="tag36h11",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

def detect():
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    detection = at_detector.detect(img = gray);
    annotated_image = gray
    for detected in detection:
        annotated_image = cv.polylines(annotated_image, pts = [detected.corners.astype(np.int32)], isClosed = True, color = (0,255,0), thickness = 2)
        annotated_image = cv.putText(annotated_image, text = f"{detected.tag_family}{detected.tag_id}", org = (detected.corners.astype(np.int32)[0][0], detected.corners.astype(np.int32)[0][1] + 20), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.4, color = (0,255,0), thickness = 1)
    # Display the resulting frame
    cv.imshow('AprilTag Detection', annotated_image)
    if cv.waitKey(1) == ord('q'):
        break

def start():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    detection = at_detector.detect(img = gray);
    annotated_image = gray
    for detected in detection:
        annotated_image = cv.polylines(annotated_image, pts = [detected.corners.astype(np.int32)], isClosed = True, color = (0,255,0), thickness = 2)
        annotated_image = cv.putText(annotated_image, text = f"{detected.tag_family}{detected.tag_id}", org = (detected.corners.astype(np.int32)[0][0], detected.corners.astype(np.int32)[0][1] + 20), fontFace = cv.FONT_HERSHEY_SIMPLEX, fontScale = 0.4, color = (0,255,0), thickness = 1)
    return annotated_image

print("AprilTag detection running...")

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        detect()
