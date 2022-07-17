import pandas as pd
import numpy as np
'''
df = pd.Series(np.arange(1,51))
#print (df)

print (df.head(5))
print (df.tail(4))
print (df.values)
'''

'''
# group by

world_cup={'Team':['West Indies','West indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','Insia','Australia'],
'Rank':[7,7,2,1,6,4,1,1,1,2,1], 
'Year':[1975,1979,1983,1987,1992,1996,1999,2003
,2007,2011,2015]}

df1 = pd.DataFrame(world_cup)
print (df1)
print (df1.groupby(['Team','Rank']).groups)
'''
'''
# concatenation
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],'ICC_rank':[2,3,7,8,4],'World_champions_Year':[2011,2015,1979,1992,1996],'Points':[874,787,753,673,855]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],'ICC_rank':[1,5,9],'Points':[895,764,656]}

df2= pd.DataFrame(world_champions)
df3 = pd.DataFrame(chokers)

print (pd.concat([df2,df3],axis=1))
'''

champion_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
'ICC_rank':[2,3,7,8,4], 
'World_champions_Year':[2011,2015,1979,1992,1996],
'Points':[874,787,753,673,855]}
match_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
'World_cup_played':[11,10,11,9,8],'ODIs_played':[733,988,712,679,662]}

df4=pd.DataFrame(champion_stats)
df5=pd.DataFrame(match_stats)
print(df4)
print(df5) 
print(pd.merge(df4,df5,on='Team'))