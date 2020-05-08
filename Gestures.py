#Perform gesture according to situation

#Takes three variables-result('w','l','t'),opponent(string),categ(string)
#Outputs a string
def perform_gesture(result,opponent,categ):
    ester_flag=ester(result,opponent,categ)
    if ester_flag==1:
        return

    if result=='w':
        print(gestures['win'][categ].format(opponent))

    if result=='l':
        print(gestures['lose'][categ].format(opponent))

    else:
        print("""You and {} are rated the same level of {}.That's really interesting!
        Better go and kiss him after this.""".format(opponent,categ))


def ester(result,opponent,categ):
    if result=='w' and opponent=='pushpanshu' and categ=='size':
        print("Thats why he is do not want to marry.Confidence!")
        return 1

    else:
        return 0