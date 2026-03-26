import argparse
import cv2
from src.detection import VehicleDetector

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    
    args = parser.parse_args()

    print(f"Processing video: {args.input}")
    print(f"Saving output to: {args.output}")

    # Initialize detector
    detector = VehicleDetector()

    # Open video
    cap = cv2.VideoCapture(args.input)

    if not cap.isOpened():
        print("❌ Error: Could not open video.")
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Handle FPS issue (important!)
    if fps == 0:
        fps = 20

    # Define VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

    # Processing loop
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("❌ No frames read. Exiting...")
            break

        results = detector.detect(frame)
        annotated = results[0].plot()

        cv2.imshow("Output", annotated)
        out.write(annotated)

        if cv2.waitKey(25) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()