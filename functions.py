categs=['smartness','sanity','gplpower','hawas','bookfetish','size']
players=['sahil','pushpanshu']

def get_initiation_input():
    input=input("Hi!type 'start' to get started")
    input=input.lower()
    if 'start' in input:
        return
    else:
        get_initiation_input()


def get_contender():
    input=input("Enter your name:")
    input=input.lower()
    if input in players:
        return input
    else:
        print('Not a valid player')
        get_contender()

#Pops the elm from the list
def pop_elm(list,elm):
    list = list.pop(list.index(elm))
    return list


def get_ans_categ(opp,valid_categs):
    print("Your opponent is",opp.capitalize())
    all_categs=','join(valid_categs)
    print("Choose a category in which you think you can defeat the opponent:",all_categs)
    input=input()
    input=input.lower()
    if input in valid_categs:
        return input
    elif input in categs:
        print("You have to wait twice before choosing a categ")
    else:
        print('Instructions follow nhi kiye jate kya Chutiye')
    get_ans_categ()


prev_categ='not assigned'
even_prev_categ='not assigned'
def set_valid_categ(valid_categ,chosen_categ):
    if even_prev_categ != 'not assigned'
        valid_categ=valid_categ.append(even_prev_categ)
    even_prev_categ = prev_categ
    prev_categ=chosen_categ
    valid_categ=pop_elm(valid_categ,chosen_categ)
    return valid_categ