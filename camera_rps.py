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
    font = cv2.FONT_HERSHEY_COMPLEX
    text_x_loc = int((cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2)-70)
    text_y_loc = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)
    
    while True:
        ret, frame = cap.read() 
        current_time = time.time()
        cv2.putText(frame,f"User : Computer",(20,17),font,0.45,(255,153,0),1)
        cv2.putText(frame,f" {user_score}  :  {computer_score} ",(15,40),font,0.75,(255,153,0),2)
        if end_time - current_time >= time_added - 2 and end_time - current_time >= time_added/2:
            cv2.putText(frame, "Start", (text_x_loc,text_y_loc),font,2,(51, 204, 51),2)
        elif end_time - current_time <= time_added/3 and end_time - current_time >= 0.9:
            cv2.putText(frame, str(round(end_time - current_time,0)),(text_x_loc,text_y_loc), font, 2, (0,0,255),2)
        elif end_time - current_time <= 0.9 and end_time - current_time > 0:
            cv2.putText(frame,"Shoot",(text_x_loc,text_y_loc), font, 2, (0,0,255),2)
        elif end_time - current_time > 0 and end_time - current_time >= time_added/3:
            cv2.putText(frame, str(round(end_time - current_time,0)), (text_x_loc,text_y_loc),font,2,(51, 153, 255),2)
        
        if end_time - current_time <= 0.05 and end_time - current_time > -0.05:
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
            print(prediction)
            print(user_choice)
            winner = get_winner(user_choice,comp_choice)
            #print(end_time- current_time)
            # Press q to close the window
        elif end_time - current_time <= -10.1 or cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif end_time - current_time <= -0.05 and end_time - current_time >= -5:
            cv2.putText(frame,f"you choose {user_choice} and computer chose {comp_choice}",(text_x_loc-150,text_y_loc),font,0.55,(153,153,255),1)    
        elif end_time - current_time <= -5 and end_time - current_time >= -10: 
            if winner[0] == 1 and winner[1] == 1:
                cv2.putText(frame,"You did not show anything",(text_x_loc-140,text_y_loc),font,1,(204,51,0),1)
            elif winner[0] == 1:
                cv2.putText(frame,"You won this round",(text_x_loc-100,text_y_loc),font,1,(204,51,0),1)
            elif winner[0] == 0 and winner[1] == 0:
                cv2.putText(frame,"It is a draw",(text_x_loc-50,text_y_loc),font,1,(204,51,0),1)
            else:
                cv2.putText(frame,"You lost this round",(text_x_loc-100,text_y_loc),font,1,(204,51,0),1)
            
        #elif end_time - current_time <= -5:
            #cv2.putText(frame, f'Your score is {user_score} and the computer score is {computer_score}',(text_x_loc-100,text_y_loc),font,0.5,(51, 153, 255),2)
            
        

        cv2.imshow('Rock Paper Scissors Game', frame)
        
            
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
        user_wins += 1
        computer_wins += 1
        return [user_wins, computer_wins]
    else:
        print("You lost")
        computer_wins += 1
        return [user_wins, computer_wins]   
        
def play():
    global cap, model, user_score, computer_score, comp_choice
    user_score = 0
    computer_score = 0 
    cap = cv2.VideoCapture(0)
    model = load_model('keras_model.h5')
    while True:
        comp_choice = get_computer_choice()
        user_pred = get_prediction()
        print(f"you chose {user_pred} and computer chose {comp_choice}")
        winner = get_winner(user_pred,comp_choice)
        print(winner)
        if winner[0] == 1 and winner[1] == 1:
            pass
        elif winner[0] == 1:
            user_score += 1
            print(f'Your score is {user_score} and the computer score is {computer_score}')
            if user_score == 3:
                print("You have won")
                restart_game = input("Do you wan to play again (Y/N): ")
                if restart_game.lower() == "y":
                    user_score = 0 
                    computer_score = 0
                else:
                    break
        elif winner[1] == 1:
            computer_score += 1
            print(f'Your score is {user_score} and the computer score is {computer_score}')
            if computer_score == 3:
                print("You have lost")
                restart_game = input("Do you wan to play again (Y/N): ")
                if restart_game.lower() == "y":
                    user_score = 0 
                    computer_score = 0
                else:
                    break
        elif winner[0] == 0 and winner[1] == 0:
            pass
                
    cap.release()
    cv2.destroyAllWindows()  
            
play()

