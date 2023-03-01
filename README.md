# **Rock Paper Scissors Game using Computer Vision and Deep Learning**
The "Rock Paper Scissors" game is a classic game that has been enjoyed by people of all ages for generations. In this project, we have developed a Python program that allows you to play this game against a computer using a webcam. The game utilises computer vision to recognise your hand gestures. This is done by using OpenCV library to capture the video frames from your webcam, and then pre-process them to feed into a pre-trained image classification model developed using [Teachable-machine](https://teachablemachine.withgoogle.com/). The computer's choice is randomly selected, and the winner is determined according to the rules of the game.
## Prerequisites
* Python 3.6 or higher
* OpenCV2 
* Keras
* Numpy
* Camera

## How to Play
To play, follow these steps:

1) Clone this repository onto your local machine

    ```bash
    git clone https://github.com/username/rock-paper-scissors.git
    cd rock-paper-scissors
    ```

2) Install dependencies using configuration file

    ```console
    conda create --name env_name python=3.8
    conda activate env_name
    pip install -r requirements.txt
    ```
3) Run the game

    ```console
    python rps_class.py
    ```

4) The program will begin by showing you the live camera feed and count down from 15 seconds. Position your hand to show either rock,paper or scissors to the camera.
5) When the timer reaches 0, the program will take a pictyure of your hand and determine whether you showed rock, paper or scissors.
6) The program will then display the computer's choice and tell you whether you won, lost or tied the game.
7) The program will round for best of 3 rounds before asking if you would like to play again or not. If you wouldn't like to play again the program will terminate.