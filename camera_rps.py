import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    comp_choice = random.choice(["rock","paper","scissors"])
    return comp_choice

def get_prediction():
    #model = load_model('keras_model.h5')
    #cap = cv2.VideoCapture(0)
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
        
        if end_time - current_time <= 0.05 and end_time - current_time > -0.05:
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
            
play()

