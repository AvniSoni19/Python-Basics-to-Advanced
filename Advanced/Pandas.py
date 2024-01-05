import pandas as pd
songs= {'Album':['Thriller','Back in Black','The Dark Side of the Moon','The Bodyguard','Bat out of the Hell'],'Released':[1982,1980,1973,1992,1977],'Length':['00:42:19','00:42:11','00:42:49','00:57:44','00:46:33']}
songs_show=pd.DataFrame(songs)
print(songs_show.head())
print('\n')
print(songs_show['Released'].unique())
print('\n')
print(songs_show['Album'][2:])
print('\n')
mid=[x for x in songs_show['Released'] if x>=1980 ]
print(mid)

df1=songs_show[songs_show['Released']>=1980]
print(df1)
df1.to_csv('1980s.csv')