import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    comp_choice = random.choice(["rock","paper","scissors"])
    return comp_choice

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    start_time = time.time()

    while start_time < start_time + 15: 
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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # After the loop release the cap object
    cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()    
            
    return user_choice


def get_winner(user_choice,computer_choice):
    
    if user_choice == "scissors" and computer_choice== "paper":
        print("You won!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == computer_choice:        print("It is a tie!")
    else:
        print("You lost")
        
def play():
    comp_choice = get_computer_choice()
    print(comp_choice)
    user_pred = get_prediction()
    print(f"you chose {user_pred}")
    get_winner(user_pred,comp_choice)

play()