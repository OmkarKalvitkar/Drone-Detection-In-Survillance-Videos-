Drone Detection in Surveillance Videos

Table of Contents
Introduction
Features
Installation
Usage
Dataset
Model Training
Results
Contributing
License
Acknowledgements
Introduction
Drone Detection in Surveillance Videos is a project that uses a fine-tuned YOLOv5 model to detect drones in real-time video feeds. This system is designed for security and surveillance purposes, providing accurate and efficient detection of aerial drones.

Features
Real-time Drone Detection: Utilizes the YOLOv5 model to detect drones in live video feeds.
High Accuracy: Fine-tuned on a custom dataset for improved detection performance.
Versatile: Can be used with webcam feeds or pre-recorded video files.
Installation
To get started with this project, follow these steps:

Clone the Repository:

sh
Copy code
git clone https://github.com/OmkarKalvitkar/Drone-Detection-In-Survillance-Videos-.git
cd Drone-Detection-In-Survillance-Videos-
Install Dependencies:

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

Training Images:

Testing Images:

Model Training
The YOLOv5 model was fine-tuned using a custom dataset. The training process involved:

Preparing the Dataset: Annotating images with bounding boxes for drones.
Training the Model: Using the YOLOv5 framework to fine-tune the pre-trained model on the custom dataset.
Validation: Evaluating the model's performance on the testing set.
Results
The trained YOLOv5 model achieved high accuracy in detecting drones in various scenarios. Below is an example of the detection result:


Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes and commit them: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-branch.
Submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Ultralytics YOLOv5 for the powerful object detection framework.
All contributors and the open-source community for their valuable resources and support.
