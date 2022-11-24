# Computer Vision Rock Paper Scissors Project

This project allows users to play rock paper scissors against a computer, where a camera is used to take in user's choice. The input from the camera is then feed into an image classifier model to determine whether the user's choice is rock, paper, scissors or nothing.
## __Milestone 1__
* Setup of Github repository to store project files. 

## __Milestone 2__

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

## __Milestone 3__

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
## __Milestone 4__
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

## __Milestone 5__ 
* Created a `get_prediction()` function to take in user input via a camera which will then be fed into the keras image model to determine the user's choice. 
* Added a timer using the `time.time()` function to capture the user's input when the timer reach 0.

    ```go
    def get_prediction():
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        # labels = []
        # with open("labels.txt") as file:
        #     for line in file:
        #         labels.append(line)
            
        # print(labels)
        
        time_added = 15
        current_time = time.time()
        end_time = time.time() + time_added

        
        while True:
            current_time = time.time()
            ret, frame = cap.read() 
            cv2.imshow('frame', frame)
            
            if end_time - current_time <= 0.05 and end_time - current_time > 0:
                print("shoot")
                ret, frame = cap.read() 
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                if np.argmax(prediction) == 0:
                    user_choice = "nothing"
                elif np.argmax(prediction) == 1:
                    user_choice = "rock"
                elif np.argmax(prediction) == 2:
                    user_choice = "paper"
                else:
                    user_choice = "scissors"
                cv2.imshow('frame', frame)
                # Press q to close the window
                print(prediction)
                print(user_choice)
                #print(end_time- current_time)
            elif end_time - current_time <= 0 or cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif end_time - current_time <= 5 and end_time - current_time > 0.1:
                print(end_time - current_time)
            
            
            
            # After the loop release the cap object
        #cap.release()
        # Destroy all the windows
        #cv2.destroyAllWindows()    
                
        return user_choice
    ```
* Created a score system by using `if` statement and `while` loops to make sure the game runs until either the user or the computer have won 3 rounds in total. 

    ```go
    def get_winner(user_choice,computer_choice):

        user_wins = 0 
        computer_wins = 0

        if user_choice == "scissors" and computer_choice== "paper":
            print("You won!")
            user_wins += 1
            return [user_wins, computer_wins]
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You won!")
            user_wins += 1
            return [user_wins, computer_wins]
        elif user_choice == "paper" and computer_choice == "rock":
            print("You won!")
            user_wins += 1
            return [user_wins, computer_wins]
        elif user_choice == computer_choice:      
            print("It is a tie!")
            return [user_wins, computer_wins]
        elif user_choice == "nothing":
            print("You did not show anything")
        else:
            print("You lost")
            computer_wins += 1
            return [user_wins, computer_wins]

    def play():
        user_score = 0
        computer_score = 0
        global cap, model
        cap = cv2.VideoCapture(0)
        model = load_model('keras_model.h5')
        while True:
            comp_choice = get_computer_choice()
            user_pred = get_prediction()
            print(f"you chose {user_pred} and computer chose {comp_choice}")
            winner = get_winner(user_pred,comp_choice)
            print(winner)
            if winner[0] == 1:
                user_score += 1
                print(f'Your score is {user_score} and the computer score is {computer_score}')
                if user_score == 3:
                    break
            elif winner[1] == 1:
                computer_score += 1
                print(f'Your score is {user_score} and the computer score is {computer_score}')
                if computer_score == 3:
                    break


        cap.release()
        cv2.destroyAllWindows()   
        ```
* Added countdown timer display on capture window.
* Allow the user to replay after either the user or computer has won.
* Added scoreboard on the top left corner of the capture window.
* Added display to show the result of the round. 