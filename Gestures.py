#Perform gesture according to situation

from all_data import *

#Takes three variables-result('w','l','t'),opponent(string),categ(string)
#Outputs a string
def perform_gesture(result,opponent,categ):
    try:
        ester_flag=ester(result,opponent,categ)
        if ester_flag==1:
            return

        if result=='w':
            try:
                print(df[df['categ']==categ].iloc[0]['lose'].format(opponent.capitalize()),'\n')
            except:
                print(df[df['categ']==categ].iloc[0]['lose'],'\n')

        elif result=='l':
            try:
                print(df[df['categ']==categ].iloc[0]['win'].format(opponent.capitalize()),'\n')
            except:
                print(df[df['categ']==categ].iloc[0]['win'],'\n')

        else:
            print("""You and {} are rated the same level in {}.That's really interesting!
            Better go and kiss him after this.""".format(opponent.capitalize(),categ),'\n')
    except:
        pass


def ester(result,opponent,categ):
    try:
        if result=='l' and opponent=='pushpanshu' and categ=='size':
            print("Thats why he do not want to marry.Confidence!\n")
            return 1

        else:
            return 0
    except:
        return 0