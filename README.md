# Traffic Violation Detection System

## 1. Project Overview

The **Traffic Violation Detection System** is a Computer Vision-based project designed to detect and annotate vehicles in traffic videos using deep learning. The current implementation uses the **YOLOv8 object detection model** to identify vehicles such as cars, motorcycles, buses, and trucks from video footage.

This project is built to be **fully executable from the command line**, making it suitable for automated evaluation environments. It processes an input video, performs vehicle detection frame by frame, and saves an annotated output video.

The system is designed in a **modular structure**, allowing future integration of advanced traffic monitoring features such as:

- Lane violation detection
- Red signal jumping detection
- Helmet detection
- Vehicle tracking
- Automated traffic rule analysis



## 2. Objectives

The main objectives of this project are:

- To build a practical **Computer Vision application** for traffic surveillance
- To detect vehicles from traffic video footage using **YOLOv8**
- To generate an annotated output video showing detected vehicles
- To create a project that is **easy to execute from terminal**
- To demonstrate concepts from the Computer Vision syllabus in a real-world application



## 3. Features

### Implemented Features
- Vehicle detection using **YOLOv8**
- Video frame processing using **OpenCV**
- Annotated output video generation
- Command-line based execution
- Optional live output display during processing
- Automatic output directory creation
- Input file existence checking

### Planned / Future Enhancements
- Lane detection using edge detection and Hough transform
- Vehicle tracking using SORT/DeepSORT
- Lane crossing violation detection
- Helmet and safety gear detection
- Traffic signal violation detection



## 4. Technologies Used

The project is implemented using the following technologies:

- **Python**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **NumPy**
- **Pandas**



## 5. Project Structure

The project follows a modular and organized structure:

```text
traffic-violation-detector/
│
├── data/
│   ├── input/              # Input videos
│   └── output/             # Processed output videos
│
├── models/                 # Reserved for custom model files
│
├── src/
│   ├── __init__.py
│   ├── detection.py        # Vehicle detection logic
│   ├── lane_detection.py   # Lane detection logic (future extension)
│
├── main.py                 # Main CLI execution file
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation
├── report/                 # Project report files
└── yolov8n.pt              # YOLOv8 pretrained model
```

## 6. System Requirements

Before running the project, ensure the following are installed on your system:

Python 3.9 or above
pip
Operating System:
 - Windows
 - Linux
 - macOS



## 7. Environment Setup

Follow these steps carefully to set up the project.

### Step 1: Clone or Download the Repository

If using Git:

git clone <https://github.com/aastha-sriv18/Traffic-Violation-Detector>
cd traffic-violation-detector

If not using Git:

Download the project ZIP
Extract it
Open the extracted folder in terminal

### Step 2: Create a Virtual Environment

Creating a virtual environment is recommended to avoid dependency conflicts.

#### For Windows
python -m venv venv
venv\Scripts\activate

#### For Linux / macOS
python3 -m venv venv
source venv/bin/activate

Once activated, your terminal should show the environment name, for example:

(venv)

### Step 3: Install Required Dependencies

Install all required Python libraries using:

pip install -r requirements.txt



## 8. Required Dependencies

The project depends on the following Python libraries:

- opencv-python
- ultralytics
- numpy
- pandas



## 9. Input Setup

Before running the project, place your input traffic video inside the following folder:

data/input/

Important Notes:
The input must be a valid video file
Recommended formats:
.mp4
.avi
.mov
Ensure the filename and extension are correct



## 10. How to Run the Project

The project is designed to run entirely from the command line.

### Basic Execution

Run the following command:

python main.py --input data/input/test.mp4 --output data/output/out.mp4

This will:

- Read the input video
- Perform vehicle detection on each frame
- Save the annotated output video in the data/output/ folder 
