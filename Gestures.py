#Perform gesture according to situation

import pandas as pd
df=pd.read_csv('gestures.csv')

#Takes three variables-result('w','l','t'),opponent(string),categ(string)
#Outputs a string
def perform_gesture(result,opponent,categ):
    ester_flag=ester(result,opponent,categ)
    if ester_flag==1:
        return

    if result=='w':
        print(df[df['categ']==categ].iloc[0]['win'].format(opponent))

    elif result=='l':
        print(df[df['categ']==categ].iloc[0]['lose'].format(opponent))

    else:
        print("""You and {} are rated the same level of {}.That's really interesting!
        Better go and kiss him after this.""".format(opponent,categ))


def ester(result,opponent,categ):
    if result=='w' and opponent=='pushpanshu' and categ=='size':
        print("Thats why he do not want to marry.Confidence!")
        return 1

    else:
        return 0