import pandas as pd
import json
import os

def get_breakup(course, department, paper):
    exists = os.path.isfile('./data/' + course + '/' + department + '/' + paper + '/' + 'breakup.csv')
    if not exists:
        return "not found", 404
    df = pd.read_csv('./data/' + course + '/' + department + '/' + paper + '/' + 'breakup.csv', encoding = 'cp1252')
    return df, 201

def get_legend(course, department, paper):
    exists = os.path.isfile('./data/' + course + '/' + department + '/' + paper + '/' + 'legend.csv')
    if not exists:
        print ("this file does not exist ", exists, ' ', './data/' + course + '/' + department + '/' + paper + '/' + 'legend.csv')
        return "not found", 404
    df = pd.read_csv('./data/' + course + '/' + department + '/' + paper + '/' + 'legend.csv', encoding = 'cp1252')
    return df, 201

def get_paperConfig(course, department, paper):
    exists = os.path.isfile('./data/' + course + '/' + department + '/' + paper + '/' + 'paperConfig.csv')
    if not exists:
        return "not found", 404
    df = pd.read_csv('./data/' + course + '/' + department + '/' + paper + '/' + 'paperConfig.csv', encoding = 'cp1252')
    return df, 201

def get_qBank(course, department, paper):
    exists = os.path.isfile('./data/' + course + '/' + department + '/' + paper + '/' + 'qBank.csv')
    if not exists:
        return "not found", 404
    df = pd.read_csv('./data/' + course + '/' + department + '/' + paper + '/' + 'qBank.csv', encoding = 'cp1252')
    return df, 201

def df_to_json(df):
    return df.to_json(orient = 'records')

#print(get_breakup('UG', 'ent' , '117').head())
#print(get_legend('UG', 'ent' , '117').head())
#print(get_paperConfig('UG', 'ent' , '117').head())
#print(get_qBank('UG', 'ent' , '117').head())



#print(df)

#print(df_to_json(df))