from all_data import *

def get_initiation_input():
    inp=input("Hi!type 'start' to get started: ")
    print()
    inp=inp.capitalize()
    if 'Start' in inp:
        return
    else:
        get_initiation_input()


def ask_difficulty():
    inp=input("Choose difficulty: Easy,Medium,Hard: ")
    print()
    inp=inp.capitalize()
    val_difs=['Easy','Medium','Hard']
    if inp in val_difs:
        return inp
    else:
        print("Not a valid input!\n")
    return ask_difficulty()


def ask_n_of_opps():
    global players
    inp=input("Type number of opponents you would like to play against: ")
    print()
    try:
        inp=int(inp)
    except:
        print("String kahe daal rhe ho\n")
        return ask_n_of_opps()
    if inp > len(players)-1:
        print("total number of players are only ",len(players))
        print("Choose a number less than that\n")
        return ask_n_of_opps()
    if inp <= 0:
        print("Chutiya hai kya?\n")
        return ask_n_of_opps()
    return inp


def get_contender():
    inp=input("Enter your name:")
    print()
    inp=inp.capitalize()
    if inp in players:
        return inp
    else:
        print('Not a valid player!\n')
        return get_contender()

#Pops the elm from the list
def pop_elm(list,elm):
    list.pop(list.index(elm))
    return list


def get_ans_categ(opp,valid_categs):
    print("Your opponent is:\n",opp.capitalize(),'\n')
    all_categs=','.join(valid_categs)
    print("Choose a category in which you think you can defeat the opponent:\n",all_categs)
    inp=input()
    print()
    inp=inp.lower()
    if inp in valid_categs:
        return inp
    elif inp in categs:
        print("Not a valid categ as per your difficulty\n")
    else:
        print('Instructions follow nhi kiye jate kya Chutiye\n')
    return get_ans_categ(opp,valid_categs)


prev_categ='not assigned'
even_prev_categ='not assigned'
def set_valid_categ(valid_categ,chosen_categ,difficulty):
    global prev_categ
    global even_prev_categ
    valid_categ=pop_elm(valid_categ,chosen_categ)
    if difficulty=='Easy':
        valid_categ.append(chosen_categ)
    if difficulty=='Medium' and prev_categ != 'not assigned':
        valid_categ.append(prev_categ)
    if difficulty=='Hard' and even_prev_categ != 'not assigned':
        valid_categ.append(even_prev_categ)
    even_prev_categ = prev_categ
    prev_categ=chosen_categ
    return valid_categ


def get_result(contender,opponent,chosen_categ):
    cont_points=data.loc[contender,chosen_categ]
    opp_points=data.loc[opponent,chosen_categ]
    if cont_points>opp_points:
        return 'w'
    elif cont_points<opp_points:
        return 'l'
    else:
        return 't'