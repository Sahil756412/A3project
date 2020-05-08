#Perform gesture according to situation

#Takes three variables-result('w','l','t'),opponent(string),categ(string)
#Outputs a string
def perform_gesture(result,opponent,categ):
    if result=='w':
        print(gestures['win'][categ].format(opponent))

    if result=='l':
        print(gestures['lose'][categ].format(opponent))

    else:
        print("""You and {} are rated the same level of {}.That's really interesting!
        Better go and kiss him after this.""".format(opponent,categ))
