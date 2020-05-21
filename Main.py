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
import random
from Gestures import *
from functions import *

#Load all files
from all_data import *

#Take input and check for keywords
get_initiation_input()

#Ask for name
contender=get_contender()

#Ask number of of opponents
n_of_opps=ask_n_of_opps()

#Ask difficulty
difficulty=ask_difficulty()

#Get into loop
valid_opponents=players.copy()
valid_opponents=pop_elm(valid_opponents,contender)
valid_categ=categs.copy()
no_of_matches=0
while True:
    no_of_matches+=1
    #Give opponent
    opponent=random.choice(valid_opponents)
    valid_opponents = pop_elm(list(valid_opponents),opponent)

    #Take answers
    while True:
        chosen_categ=get_ans_categ(opponent,valid_categ)
        valid_categ=set_valid_categ(valid_categ,chosen_categ,difficulty)

        #process it
        result=get_result(contender,opponent,chosen_categ)
        if result != 'w' and result != 'l':
            perform_gesture(result, opponent, chosen_categ)
            continue
        break
    if result=='w':
        print('You win\n')
    else:
        print('You lose\n')
    perform_gesture(result, opponent, chosen_categ)
    if len(valid_opponents)==0 or result=='l' or no_of_matches==n_of_opps:
        break

if result=='w':
    print('Congratulations! You defeated all of the {} opponents\n'.format(n_of_opps))
else:
    print('You defeated {} opponents'.format(no_of_matches-1))
print('Here, have this')
print('c=3')
if result=='w':
    print('anyways')