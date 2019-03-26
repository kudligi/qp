import pandas as pd
import json

def get_breakup(course, department, paper):
    df = pd.read_csv('../data/' + course + '/' + department + '/' + paper + '/' + 'breakup.csv', encoding = 'cp1252')
    return df

def get_legend(course, department, paper):
    df = pd.read_csv('../data/' + course + '/' + department + '/' + paper + '/' + 'legend.csv', encoding = 'cp1252')
    return df

def get_paperConfig(course, department, paper):
    df = pd.read_csv('../data/' + course + '/' + department + '/' + paper + '/' + 'paperConfig.csv', encoding = 'cp1252')
    return df

def get_qBank(course, department, paper):
    df = pd.read_csv('../data/' + course + '/' + department + '/' + paper + '/' + 'qBank.csv', encoding = 'cp1252')
    return df

def df_to_json(df):
    return df.to_json(orient = 'records')

#print(get_breakup('UG', 'ent' , '117').head())
#print(get_legend('UG', 'ent' , '117').head())
#print(get_paperConfig('UG', 'ent' , '117').head())
#print(get_qBank('UG', 'ent' , '117').head())

df = get_qBank('UG', 'ent' , '117').head()

print(df)

print(df_to_json(df))