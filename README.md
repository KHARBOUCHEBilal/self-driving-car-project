# Autonomous Car Project

## Description
This project involves the development of an autonomous car system using Raspberry Pi and NVIDIA Jetson Nano. The system leverages computer vision, machine learning, and robotics to navigate through various environments autonomously. 

### Objectives
- To design and implement an autonomous car capable of navigating different terrains.
- To utilize Raspberry Pi for initial prototyping and data collection.
- To transition to NVIDIA Jetson Nano for enhanced processing power and advanced machine learning capabilities.
- To integrate sensors and cameras for real-time data acquisition and processing.

## Technologies Used
- **Raspberry Pi**: Initial platform for prototyping and basic functionalities.
- **NVIDIA Jetson Nano**: Main processing unit for advanced computation and deep learning.
- **OpenCV**: Library for computer vision tasks.
- **TensorFlow/Keras**: Frameworks for implementing machine learning models.
- **Python**: Programming language for developing the software components.

## Features
- **Real-time Object Detection**: Ability to identify and track objects in the environment.
- **Path Planning**: Algorithms to navigate around obstacles.
- **Sensor Integration**: Use of LIDAR, ultrasonic sensors, and cameras for environment perception.
- **Remote Control**: Manual override option through a web interface or mobile app.

## Getting Started

### Prerequisites
- Raspberry Pi with Raspbian OS
- NVIDIA Jetson Nano with JetPack installed
- Required Python libraries:
  ```bash
  pip install opencv-python tensorflow keras
  ```

### Installation
1. **Raspberry Pi Setup**:
   - Install the necessary libraries and dependencies.
   - Connect the sensors and cameras to the Raspberry Pi.

2. **NVIDIA Jetson Nano Setup**:
   - Install JetPack and configure the Jetson Nano.
   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/autonomous-car.git
     cd autonomous-car
     ```

3. **Data Collection**:
   - Use the Raspberry Pi to collect data for training machine learning models.
   - Store the collected data for later use on the Jetson Nano.

### Usage
To run the autonomous car application:
```bash
python main.py
```

- Follow the prompts for manual control or allow the car to navigate autonomously.

## Code Structure
- `main.py`: Main application file to control the car.
- `camera.py`: Code for handling camera input.
- `sensor.py`: Code for processing sensor data.
- `model.py`: Machine learning model for object detection and navigation.
- `README.md`: Documentation for the project.

## References
- [NVIDIA Jetson Nano Documentation](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
- [OpenCV Documentation](https://docs.opencv.org/)

## Author
- **Kharbouche Bilal**  
  Email: bilal.kharbouche99@gmail.com
