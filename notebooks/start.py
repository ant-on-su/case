#%% [markdown]
# # Airbnb case

#%%
import pandas as pd
import numpy as np
import pandas_profiling

#%%
df=pd.read_csv('./data/listings.csv')
df.head()

#%%
pandas_profiling.ProfileReport(df).to_file(
outputfile='./output/pd-profiling.html')

#%%
pd.to_datetime(df['last_review'])
df.dtypes