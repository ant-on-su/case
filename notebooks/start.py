#%% [markdown]
# # Airbnb case

#%%
import pandas as pd
import numpy as np
import pandas_profiling

#%%
df=pd.read_csv('../data/listings.csv')
df.head()

#%%
df['last_review']=pd.to_datetime(df['last_review'], yearfirst=True)
df.dtypes

#%%
df['months_exist']=df['reviews_per_month']*df['number_of_reviews']
df.head()

#%%
pandas_profiling.ProfileReport(df).to_file(
outputfile='../output/pd-profiling.html')
