import pandas as pd
import numpy as np



world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],'ICC_rank':[2,3,7,8,4],'World_champions_Year':[2011,2015,1979,1992,1996],'Points':[874,787,753,673,855]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],'ICC_rank':[1,5,9],'Points':[895,764,656]}

df1 = pd.DataFrame(world_champions)
df2 = pd.DataFrame(chokers)

# left outer join 
print (pd.merge(df1,df2,on="Team",how="left"))

# right outer join
print (pd.merge(df1,df2,on="Team",how="right"))

# inner join 
print (pd.merge(df1,df2,on="Team",how="inner"))

# full outer join
print (pd.merge(df1,df2,on="Team",how="outer"))