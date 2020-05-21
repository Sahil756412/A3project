import pandas as pd
df=pd.read_csv('gestures.csv')
data=pd.read_csv('points_data.csv')
data=data.set_index(['players'])
categs=list(data.columns[1:])
players=list(data.index)