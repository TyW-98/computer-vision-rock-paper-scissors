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
* Created a `get_computer_choice()` function where `random.choice()` was used to randomly pick the computer's choice.
  
    ```go
    def get_computer_choice():
    comp_choice = random.choice(["rock","paper","scissors"])
    return comp_choice
    ```
* Created a `get_user_choice()` function which uses `input()` to ask user to input their choice of rock,paper or scissors. 

    ```go
    def get_user_choice():
    choice = input("Rock, Paper or Scissors? : ")
    return choice
    ```
* Created a `get_winner()` function which uses `get_computer_choice()` and `get_user_choice()` to determine the winner of the round. 
  * If the user wins, it will print "You Won!". 
  * If the computer wins, it will print "You Lost"
  * IF the user and computer chooses the same option, it will print "It is a tie!" 

  ```go
    def get_winner(user_choice,computer_choice):

    if user_choice == "scissors" and computer_choice== "paper":
        print("You won!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == computer_choice:
        print("It is a tie!")
    else:
        print("You lost")
  ```
* Created a `play()` function to call the three function created. 

    ```go
    def play():
    comp_choice = get_computer_choice()
    print(comp_choice)
    user_choice = get_user_choice()
    print(user_choice)
    get_winner(user_choice,comp_choice)
    ```