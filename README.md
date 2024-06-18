
# Drone Detection in Surveillance Videos

![Drone Detection](images/Screenshot-2024-04-03-190515.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Drone Detection in Surveillance Videos is a project that uses a fine-tuned YOLOv5 model to detect drones in real-time video feeds. This system is designed for security and surveillance purposes, providing accurate and efficient detection of aerial drones.

## Features
- **Real-time Drone Detection:** Utilizes the YOLOv5 model to detect drones in live video feeds.
- **High Accuracy:** Fine-tuned on a custom dataset for improved detection performance.
- **Versatile:** Can be used with webcam feeds or pre-recorded video files.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/OmkarKalvitkar/Drone-Detection-In-Survillance-Videos-.git
   cd Drone-Detection-In-Survillance-Videos-
## Install Dependencies:

sh
Copy code
    pip install -r requirements.txt
    Download the YOLOv5 Model:

Download the pre-trained YOLOv5 model from this link and place it in the project directory.
Usage
Run the Detection Script:

sh
Copy code
python Advanced_Drone_Detection.py
Video Source:

The default video source is set to the webcam (cv2.VideoCapture(0)). To change the source, modify the cap variable in Advanced_Drone_Detection.py.
Dataset
The dataset used for training the model consists of various images and videos of drones captured in different environments. The dataset is divided into training and testing sets.

## Training Images: ![Screenshot 2024-04-04 104812](https://github.com/OmkarKalvitkar/Drone-Detection-In-Survillance-Videos-/assets/161920873/18cbb27e-ddbf-4a30-9025-2ea0f0477a6d)


## Testing Images: ![Screenshot 2024-04-03 190515](https://github.com/OmkarKalvitkar/Drone-Detection-In-Survillance-Videos-/assets/161920873/87e8fce1-ee6b-4dd5-9b5c-5740070b9d35)


Model Training
The YOLOv5 model was fine-tuned using a custom dataset. The training process involved:

Preparing the Dataset: Annotating images with bounding boxes for drones.
Training the Model: Using the YOLOv5 framework to fine-tune the pre
