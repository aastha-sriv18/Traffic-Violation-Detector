import cv2
from src.detection import VehicleDetector

detector = VehicleDetector()

cap = cv2.VideoCapture(args.input)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect(frame)

    annotated = results[0].plot()
    cv2.imshow("Output", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break