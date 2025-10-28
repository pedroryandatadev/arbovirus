import pandas as pd
from columns import columns_delete

df = pd.read_csv('data/interim/join.csv', dtype_backend='numpy_nullable')
df.drop(columns=columns_delete, inplace=True, errors='ignore')

df = df.dropna()

df.to_csv('data/interim/clean_data.csv', index=False)