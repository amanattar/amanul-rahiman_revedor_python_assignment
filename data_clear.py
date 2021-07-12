import pandas as pd
import json

df = pd.read_json('data.json', lines=True)

df.rename(columns={'a': 'address', 'liid': 'linkedin_id', 'linkedin':'profile_url', 'n':'name', 't':'mob_number', 'e':'email'}, inplace=True)
df = df[pd.notnull(df['address'])]
df = df.reset_index()

data_sample = df

data_sample['id'] = ""
for i in range(len(data_sample['linkedin_id'])):
    data_sample['id'][i] = i+1

data_main = data_sample[['id','linkedin_id','address','profile_url']]

data_email = data_sample[['id','linkedin_id','email']]
data_email = data_email[pd.notnull(data_email['email'])]

data_number = data_sample[['id','linkedin_id','mob_number']]
data_number = data_number[pd.notnull(data_number['mob_number'])]

data_main.to_csv("data_main.csv",index=False)
data_email.to_csv("data_email.csv",index=False)
data_number.to_csv("data_number.csv",index=False)