# Sign Language To Text

This repository contains a computer vision model that can categorize sign language gestures into 9 different categories. The model is trained on a custom dataset and achieves high accuracy in categorizing sign language gestures.

## Features

* Accuracy: The model achieves 99.1% accuracy on the test data
* Easy to Use: This repo comes with `inference.py` file which uses the camera and categorizes real-time video data

## Dataset

The dataset used to train the model consists of 241 image all created manually via `datacollect.py` and stored in `data` folder

**Important Note 1:** You have to open the directory in the terminal and execute the following commands
**Important Note 2:** You have to install Python 3.10.6
# How to Use
## Installtion
To install the dependencies, run:
`pip install -r requirements.txt`
## Usage
To use your camera to categorize realtime video data of sign language, run:
`python inference.py`
This will open a window showing camera, make a gesture with your hand and it will put a box around your hand with the category on it

# How it Works
## Collecting Images
To collect Images of yourself doing gestures of sign languages, run:
`python datacollect.py`
This python file opens the camera, wait for **5** seconds at the start and then take `imgnums` images (number of images). There's a **2** second-cooldown between each image (Try to put your hand in a different place in order for the dataset to be as diverse as possible). Feel Free to change those variables to suit your needs

## Training
All of the training process is in `train.ipynb`. First the data (collected before) is loaded into the memory. Each image is converted into 12 images by doing Data Augmentation (Rotating, Flipping, Zomming, etc..), The images then go into mediapipe to detect the landmarks of the hand in each image. These landmarks are then reepresented as a single list for each image with shape (21, 3). These lists are then splitted into train and test data and then passed into the neural network for training. Early Stopping and Dropout layers are used in order to reduce overfitting. The model is then saved in a file.
Feel free to tune parameters in `train.ipynb` to suit your needs.
