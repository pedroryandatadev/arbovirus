import pandas as pd
from columns import columns_dict

ages = range(2016, 2025)
files = [f'data/raw/chikon{ano}.csv' for ano in ages] + \
           [f'data/raw/dengon{ano}.csv' for ano in ages]

dfs = []

for path in files:
    try:
        # Detect separator
        with open(path, 'r', encoding='utf-8') as f:
            sep = ';' if ';' in f.readline() else ','
        
        df = pd.read_csv(path, sep=sep)
        df.columns = df.columns.str.strip().str.lower()
        df = df.rename(columns=columns_dict)
        
        # Ensure all dictionary columns exist
        for col in columns_dict.values():
            if col not in df.columns:
                df[col] = pd.NA

        dfs.append(df)
    except FileNotFoundError:
        print(f'❌  File not found -> {path}')

# Concatenate DataFrames
df_final = pd.concat(dfs, join='inner')

# Convert numeric columns to Int64
for col in df_final.select_dtypes(include='number'):
    df_final[col] = df_final[col].astype('Int64')

df_final.to_csv('data/interim/join.csv', index=False)