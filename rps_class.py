import random
import cv2
from keras.model import load_model
import numpy as np
import time

class rps:
    
    def __init__(self,user_score = 0, computer_score = 0):
        self.computer_score = computer_score
        self.user_score = user_score
        self.cap = cv2.VideoCapture(0)
        self.model = load_model("keras_model.h5")
        
    def get_computer_choice(self):
        comp_choice = random.choice(["rock","paper","scissors"])
        return comp_choice
    
    def get_prediction():
        pass