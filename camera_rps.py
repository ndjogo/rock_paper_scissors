import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#funciton for computer to select random option
computer_choice = ""
def get_computer_choice(): 
    global computer_choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    return computer_choice
   
#function to retreive user choice 
user_choice = "" 
def get_prediction():
    global user_choice
    highest_prob = max(prediction[0])
    if prediction[0][0] == highest_prob:
        correct_prediction = "Rock"
    elif prediction[0][1] == highest_prob:
        correct_prediction = "Paper"
    elif prediction[0][2] == highest_prob:
        correct_prediction = "Scissors"
    else: 
        correct_prediction = "Nothing"
    user_choice = correct_prediction 
    return user_choice 

#counters for the game 
user_wins = 0 
computer_wins = 0 
draw = 0 

#tracks winner after each round and updates counters
def get_winner(computer_choice, user_choice):
    global draw, user_wins, computer_wins
    if computer_choice == "Rock" and user_choice == "Rock":
        draw += 1 
    elif computer_choice == "Rock" and user_choice == "Scissors":
        computer_wins += 1
    elif computer_choice == "Rock" and user_choice == "Paper":
        user_wins += 1
    elif computer_choice == "Paper" and user_choice == "Rock":
        computer_wins += 1
    elif computer_choice == "Paper" and user_choice == "Scissors":
        user_wins += 1
    elif computer_choice == "Paper" and user_choice == "Paper":
        draw += 1
    elif computer_choice == "Scissors" and user_choice == "Rock":
        user_wins += 1
    elif computer_choice == "Scissors" and user_choice == "Scissors":
        draw += 1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        computer_wins += 1
    elif user_choice == "Nothing": 
        draw += 1 


#we are playing 5 rounds 
for rounds in range(5):
    for i in range(180):
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
    
        # countdown timer   
        if i//30 < 3:
            frame = cv2.putText(frame,str(i//30+1),(320,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,250,0),2,cv2.LINE_4)

        # get user prediction and computer prediction after countdown and then update score trackers
        elif i/30 == 4:
            prediction = model.predict(data)
            get_prediction()
            get_computer_choice() 
            get_winner(computer_choice, user_choice)

        #adding text and scores to the video
        frame = cv2.putText(frame,"User: {} Computer: {} Draw: {}".format(user_wins,computer_wins,draw),(120,400),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4)
        frame = cv2.putText(frame,"User Played:{}".format(user_choice),(10,140),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4)
        frame = cv2.putText(frame,"Computer Played: {}".format(computer_choice),(270,140),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4)
        
        #display winner at the end
        if computer_wins > user_wins and computer_wins + user_wins + draw == 5: 
            frame = cv2.putText(frame,"You lose",(300,350),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4)
        elif computer_wins < user_wins and computer_wins + user_wins + draw == 5: 
            frame = cv2.putText(frame,"You win",(300,350),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4) 
        elif computer_wins == user_wins and computer_wins + user_wins + draw == 5: 
            frame = cv2.putText(frame,"It is a draw",(300,350),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,250,0),2,cv2.LINE_4)     
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
