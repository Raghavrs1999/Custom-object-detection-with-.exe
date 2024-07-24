# Real-time Object Detection

This project implements a real-time object detection system using YOLOv4-tiny and OpenCV. It allows users to detect and highlight specific objects in a video stream from a camera.

## Features

- Real-time object detection using YOLOv4-tiny
- Customizable GUI with toggleable object detection buttons
- Support for multiple object classes
- Easy-to-use executable for Windows users

## Prerequisites

- Python 3.7+
- OpenCV
- NumPy
- YOLOv4-tiny weights and configuration files
- Webcam or camera device

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Raghavrs1999/Custom-object-detection-with-.exe.git
   cd real-time-object-detection
   ```

2. Install the required dependencies:
   ```
   pip install opencv-python numpy
   ```

3. Download the YOLOv4-tiny weights and configuration files and place them in the `dnn_model` directory.

## Usage

### Using the Pre-built Executable (Windows)

1. Clone the repository as described in the Installation section.
2. Navigate to the `dist` folder.
3. Run the `Object detector.exe` file.

### Building from Source

1. Ensure you have all the prerequisites installed.
2. Run the main script:
   ```
   python "Object detector.py"
   ```

3. To create your own executable:
   ```
   python setup.py build
   ```

## How it Works

1. The program initializes the camera and loads the YOLOv4-tiny model.
2. It creates a GUI with toggleable buttons for different object classes.
3. In real-time, it processes each frame from the camera:
   - Performs object detection using the YOLOv4-tiny model
   - Checks which object classes are active (toggled on)
   - Draws bounding boxes and labels for detected objects of active classes
4. The user can click on the buttons to toggle detection for specific object classes.

## Customization

- To add or remove detectable objects, modify the `add_button` calls in `Object detector.py`.
- To change the camera source, modify the `cv2.VideoCapture(1)` line in `Object detector.py`.
- Adjust detection confidence and NMS thresholds in the `model.detect()` call for different detection sensitivity.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- YOLOv4 developers
- OpenCV communit
