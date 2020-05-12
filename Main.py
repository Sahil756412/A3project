#Chatbot
#You should put in certain keyword to call it
#It will ask for your name
#It will give a confirmation promt
#Put a keyword to start
#It will give you a contender
#Put in the field in which you think,you can beat the contender
#It will give result
#It will ask you again if you win

#Load all modules
import pandas as pd
import random
from Gestures import *
from functions import *

#Load all files
data=pd.read_csv('points_data.csv')
categs=['smartness','sanity','gplpower','hawas','bookfetish','size']
players=['sahil','pushpanshu']

#Take input and check for keywords
get_initiation_input()

#Ask for name
contender=get_contender()

#Get into loop
valid_opponents=players.copy()
valid_opponents=pop_elm(valid_opponents,contender)
valid_categ=categs.copy()
while True:
    #Give opponent
    opponent=random.choice(valid_opponents)
    valid_opponents = pop_elm(valid_opponents,opponent)

    #Take answer
    chosen_categ=get_ans_categ(opponent,valid_categ)
    valid_categ=set_valid_categ(valid_categ,chosen_categ)


    #process it
        #Compare

        #If tie
            #perform a gesture
            #Ask again by rerunning a loop

        #set the flag to win or loss

    #Give Output-
        #Give Result
        #Perform Gesture

#Give final Output