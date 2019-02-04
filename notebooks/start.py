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

#%% [markdown]
# ## Observations:
# 80% entire home -OK, 19% private, 0.5% shared room - B&B accoridng to Gemeente -check!
# Wierd extremes: 
# -minimum nights 365, 523, 1k ?
# -price 977 - 8616 p/night?!
 