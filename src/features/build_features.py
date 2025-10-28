import pandas as pd

df = pd.read_csv('data/interim/clean_data.csv')

# Treating age-related spine
# Function to convert and round/truncate
def convert_age(valor):

    valor_int = int(valor) # Ensure the value is an integer
    valor_str = str(valor_int) # Convert to string for easier splitting (used for indexing)

    unidade = int(valor_str[0]) # Get the first digit in int format (1=days, 2=weeks, 3=months, 4=years)
    quantidade = int(valor_str[1:]) # Gets the remainder of the value in int format (represents the amount of time | 012 -> 12)

    if unidade == 1:  # days
        idade = quantidade / 365
    elif unidade == 2:  # weeks
        idade = (quantidade * 7) / 365
    elif unidade == 3:  # months
        idade = quantidade / 12
    elif unidade == 4:  # years
        idade = quantidade
    else:
        return 0

    return int(idade)

# Apply age conversion
df['nu_idade'] = df['nu_idade'].apply(convert_age)

# Delete rows with zero age
df = df[df['nu_idade'] != 0]

# Map gender column to numeric values
# Map: F=0, M=1, I=2, others=3
df['tp_sexo'] = df['tp_sexo'].map({'F':0, 'M':1, 'I':2}).astype(int)

# Map symptom columns to binary values
# Mapping binary symptoms
sintomas = ['febre','mialgia','cefaleia','vomito','nausea','dor_costas','artralgia','petequia_n','dor_retro']

# Apply mapping
for col in sintomas:
    if col in df.columns:
        # 1 = yes -> 1, 2 = no -> 0, missing values ​​= 0
        df[col] = df[col].map({1:1, 2:0}).astype(int)

# Tagert (final classification)
# Map ratings to DENGUE, CHIKUNGUNYA, OTHER
mapping = {
    1: 'DENGUE', 2: 'DENGUE', 10: 'DENGUE', 11: 'DENGUE', 12: 'DENGUE',
    13: 'CHIKUNGUNYA',
    5: 'OTHER', 8: 'OTHER'
}

# Apply mapping and fill unmapped values ​​with 'OTHER'
df['tp_classificacao_final'] = df['tp_classificacao_final'].map(mapping).fillna('OTHER')

df.to_csv('data/processed/processed.csv', index=False)