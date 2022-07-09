import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

computer_choice = []
def get_computer_choice(): 
    answer = random.choice(["Rock", "Paper", "Scissors"])
    computer_choice.append(answer)



user_choice = [] 
def get_prediction(prediction):
    highest_prob = max(prediction[0])
    if prediction[0][0] == highest_prob:
        correct_prediction = "Rock"
    elif prediction[0][1] == highest_prob:
        correct_prediction = "Paper"
    elif prediction[0][2] == highest_prob:
        correct_prediction = "Scissors"
    else: 
        correct_prediction = "Nothing"
    
    user_choice.append(correct_prediction)


def get_winner(computer_choice, user_choice):

    if computer_choice[0] == "Rock" and user_choice[0] == "Rock":
        print ("This is a draw")
    elif computer_choice[0] == "Rock" and user_choice[0] == "Scissors":
        print ("The computer wins")
    elif computer_choice[0] == "Rock" and user_choice[0] == "Paper":
        print ("The user wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Rock":
        print ("The computer wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Scissors":
        print ("The user wins")
    elif computer_choice[0] == "Paper" and user_choice[0] == "Paper":
        print("This is a draw")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Rock":
        print ("The user wins")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Scissors":
        print ("This game is a draw")
    elif computer_choice[0] == "Scissors" and user_choice[0] == "Paper":
        print("The computer wins") 

    print( f"The computer's choice was: {computer_choice[0]} " )
    print( f"The user's choice was: {user_choice[0]}" )

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    get_computer_choice()
    print("COMPUTER CHOICE COMPUTER CHOICE COMPUTER CHOICE")
    print(computer_choice)
    get_prediction(prediction)
    print("USER CHOICE USER CHOICE USER CHOICE USER CHOICE")
    print(user_choice)
    get_winner(computer_choice, user_choice)
    

    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
