import pandas as pd

#Difine categs and players
categs=['smartness','sanity','gplpower','hawas','bookfetish','size']
players=['Arush','Nitish','Jindal','Vivek','Saurabh','Piyush','Vats','Shubham','Akshat','Aniket','Pushpanshu','Kedarnath','Nippon','Tejesh','Rajit','Vineet','Sahil','Nishant']
poll_data_file="Chatbot poll 2.csv"

raw_data=pd.read_csv(poll_data_file)
#make points dataframe
cols=['players']
cols+=categs
points_data=pd.DataFrame(columns=cols)
points_data['players']=players
points_data.set_index('players')
points_data=points_data.fillna(0)

#Assign points
for i,rows in raw_data.iterrows():
    points_data.loc[points_data['players']==rows['Smartness 1'],'smartness']+=5
    points_data.loc[points_data['players']==rows['Smartness 2'],'smartness']+=3
    points_data.loc[points_data['players']==rows['Smartness 3'],'smartness']+=2
    points_data.loc[points_data['players']==rows['Sanity 1'],'sanity']+=5
    points_data.loc[points_data['players']==rows['Sanity 2'],'sanity']+=3
    points_data.loc[points_data['players']==rows['Sanity 3'],'sanity']+=2
    points_data.loc[points_data['players']==rows['gplpower 1'],'gplpower']+=5
    points_data.loc[points_data['players']==rows['gplpower 2'],'gplpower']+=3
    points_data.loc[points_data['players']==rows['gplpower 3'],'gplpower']+=2
    points_data.loc[points_data['players']==rows['Hawas 1'],'hawas']+=5
    points_data.loc[points_data['players']==rows['Hawas 2'],'hawas']+=3
    points_data.loc[points_data['players']==rows['Hawas 3'],'hawas']+=2
    points_data.loc[points_data['players']==rows['bookfetish 1'],'bookfetish']+=5
    points_data.loc[points_data['players']==rows['bookfetish 2'],'bookfetish']+=3
    points_data.loc[points_data['players']==rows['bookfetish 3'],'bookfetish']+=2
    points_data.loc[points_data['players']==rows['Size 1'],'size']+=5
    points_data.loc[points_data['players']==rows['Size 1'],'size']+=3
    points_data.loc[points_data['players']==rows['Size 1'],'size']+=2

#Make points_data
points_data.to_csv('points_data.csv')