from all_data import *

def get_initiation_input():
    inp=input("Hi!type 'start' to get started ")
    inp=inp.lower()
    if 'start' in inp:
        return
    else:
        get_initiation_input()


def get_contender():
    inp=input("Enter your name:")
    inp=inp.lower()
    if inp in players:
        return inp
    else:
        print('Not a valid player')
        return get_contender()

#Pops the elm from the list
def pop_elm(list,elm):
    list.pop(list.index(elm))
    return list


def get_ans_categ(opp,valid_categs):
    print("Your opponent is",opp.capitalize())
    all_categs=','.join(valid_categs)
    print("Choose a category in which you think you can defeat the opponent:",all_categs)
    inp=input()
    inp=inp.lower()
    if inp in valid_categs:
        return inp
    elif inp in categs:
        print("You have to wait twice before choosing a categ")
    else:
        print('Instructions follow nhi kiye jate kya Chutiye')
    return get_ans_categ(opp,valid_categs)


prev_categ='not assigned'
even_prev_categ='not assigned'
def set_valid_categ(valid_categ,chosen_categ):
    global prev_categ
    global even_prev_categ
    if even_prev_categ != 'not assigned':
        valid_categ=valid_categ.append(even_prev_categ)
    even_prev_categ = prev_categ
    prev_categ=chosen_categ
    valid_categ=pop_elm(valid_categ,chosen_categ)
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