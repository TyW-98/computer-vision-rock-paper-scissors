import random
import cv2
from keras.models import load_model
import numpy as np
import time

class rps:
    
    def __init__(self,):
        self.computer_score = 0
        self.user_score = 0
        self.times_up = -10.1
        self.cap = cv2.VideoCapture(0)
        self.model = load_model("keras_model.h5")
        
        self.play()
        
    def get_computer_choice(self):
        self.comp_choice = random.choice(["rock","paper","scissors"])
        return self.comp_choice
    
    def get_prediction(self):
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        time_added = 15
        current_time = time.time()
        end_time = time.time() + time_added
        font = cv2.FONT_HERSHEY_COMPLEX
        text_x_loc = int((self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2)-70)
        text_y_loc = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)
        
        while True:
            ret, frame = self.cap.read()
            current_time = time.time()
            cv2.putText(frame,f"User : Computer",(20,17),font,0.45,(255,153,0),1)
            cv2.putText(frame,f" {self.user_score}  :  {self.computer_score} ",(15,40),font,0.75,(255,153,0),2)
            if end_time - current_time >= time_added - 2 and end_time - current_time >= time_added/2:
                cv2.putText(frame, "Start", (text_x_loc,text_y_loc),font,2,(51, 204, 51),2)
            elif end_time - current_time <= time_added/3 and end_time - current_time >= 0.9:
                cv2.putText(frame, str(round(end_time - current_time,0)),(text_x_loc,text_y_loc), font, 2, (0,0,255),2)
            elif end_time - current_time <= 0.9 and end_time - current_time > 0:
                cv2.putText(frame,"Shoot",(text_x_loc,text_y_loc), font, 2, (0,0,255),2)
            elif end_time - current_time > 0 and end_time - current_time >= time_added/3:
                cv2.putText(frame, str(round(end_time - current_time,0)), (text_x_loc,text_y_loc),font,2,(51, 153, 255),2)

            if end_time - current_time <= 0.05 and end_time - current_time > -0.05:
                resized_frame = cv2.resize(frame,(224,224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32)/ 127) - 1
                data[0] = normalized_image
                prediction = self.model.predict(data)
                if np.argmax(prediction) == 0 :
                    self.user_choice = "nothing"
                elif np.argmax(prediction) == 1:
                    self.user_choice = "rock"
                elif np.argmax(prediction) == 2:
                    self.user_choice = "paper"
                else:
                    self.user_choice = "scissors"
                    
                print(prediction)
                print(self.user_choice)
                       
                self.get_winner()
                
            elif end_time - current_time <= self.times_up or cv2.waitKey(1) & 0xFF == ord("q"):
                break
            elif end_time - current_time <= -0.05 and end_time - current_time >= -5:
                cv2.putText(frame,f"you choose {self.user_choice} and computer choose {self.comp_choice}",(text_x_loc-150,text_y_loc),font,0.55,(153,153,255),1)
            elif end_time - current_time <= -5 and end_time - current_time >= self.times_up-0.1:
                if self.user_wins == 1 and self.computer_wins == 1:
                    cv2.putText(frame,"You did not show anything",(text_x_loc-140,text_y_loc),font,1,(204,51,0),1)
                elif self.user_wins == 1:
                    cv2.putText(frame,"You won this round",(text_x_loc-100,text_y_loc),font,1,(204,51,0),1)
                elif self.user_wins == 0 and self.computer_wins == 0:
                    cv2.putText(frame,"It is a draw",(text_x_loc-50,text_y_loc),font,1,(204,51,0),1)
                else:
                    cv2.putText(frame,"You lost this round",(text_x_loc-100,text_y_loc),font,1,(204,51,0),1)
                
            cv2.imshow("Rock Paper Scissors Game", frame)
                
    def get_winner(self):
        
        self.user_wins = 0
        self.computer_wins = 0
        
        if self.user_choice == "scissors" and self.comp_choice == "paper":
            print("YOU WON!")
            self.user_wins += 1
        elif self.user_choice == "rock" and self.comp_choice == "scissors":
            print("YOU WON!")
            self.user_wins += 1
        elif self.user_choice == "paper" and self.comp_choice == "rock":
            print("YOU WON!")
            self.user_wins += 1
        elif self.user_choice == self.comp_choice :
            print("IT IS A TIE!")
        elif self.user_choice == "nothing":
            print("No user input detected by the camera")
            self.user_wins += 1
            self.computer_wins += 1
        else:
            print("YOU LOST!")
            self.computer_wins += 1
            
    def play(self):
        
        while True:
            self.get_computer_choice()
            self.get_prediction()
            print(f"you chose {self.user_choice} and computer chose {self.comp_choice}")    
            
            if self.user_wins == 1 and self.computer_wins == 1: 
                pass
            elif self.user_wins == 1:
                self.user_score += 1
                print(f'Your score is {self.user_score} and the computer score is {self.computer_score}')
                if self.user_score == 3:
                    print("YOU HAVE WON THE GAME!")
                    restart_game = input("Do you want to play again (Y/N)?: ")
                    if restart_game.lower() == "y":
                        self.user_score == 0
                        self.computer_score == 0 
                    else:
                        break
                    
            elif self.computer_wins == 1:
                self.computer_score += 1
                print(f"Your score is {self.user_score} and the computer score is {self.computer_score}")
                if self.computer_score == 3:
                    print("YOU HAVE LOST THE GAME!")
                    restart_game = input("Do you want to play again (Y/N)?: ")
                    if restart_game.lower() == "y":
                        self.user_score == 0
                        self.computer_score == 0 
                    else:
                        break 
        
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    play1 = rps()   
