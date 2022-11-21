# Computer Vision Rock Paper Scissors Project

This project allows users to play rock paper scissors against a computer, where a camera is used to take in user's choice. 
## Milestone 1
* Setup of Github repository to store project files. 

## Milestone 2

* Create an image model using [Teachable-machine](https://teachablemachine.withgoogle.com/) where the image model be used to classify 4 different classes:
  * Nothing
  * Rock
  * Paper
  * Scissors 
* The size of the test set for the image model is 15% of the dataset. The model is trained for 50 epochs with batch size of 16 and learning rate of 0.001.
* The confusion matrix shows the true positives(TP), false negative(FN), false positive(FP) and true negative(TN) of each class.  
* The confusion matrix for the image model shows that the model is able to correctly classify all the samples in the test dataset into the correct class. 
* Using the confusion matrix, the model's precision and hit-rate can be obtained as 1. 
### __Image model confusion matrix__ 
<img src = images/CM.png width = "350">

* The loss graph illustrates the summation of errors in the model as number of epochs increases. 
* From the loss graph, it can be observed that after a few epochs the loss value of the model is very close to 0. This means that the model is able to predict the clases with few errors. 

### __Keras model loss graph__
<img src = images/Loss_graph.png width = "350">

* The model is then download as a Keras model.

## Milestone 3

* Create new virtual environment 
    ```go
    conda create --name env_name python = 3.8
    ```
* Install the necessary libraries
    ```go
    pip install opencv-python
    pip install tensorflow
    pip install ipykernel
    ```
* Familaries with `RPS-Template.py`
## Milestone 4
* 