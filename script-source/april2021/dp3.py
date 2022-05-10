import pandas as pd
import os
import sys
from constants import *
from util import *
from new_paper import *
import numpy as np

def f(x):
    return ''.join(filter(lambda i: i.isdigit(), x))

root_path=sys.argv[1]
print(root_path)
if "cbme" in root_path:
    print(os.path.join(root_path, "mcq.csv"))
    # MCQ QBANK:

    df = read_csv_generic(COLUMNS_QBANK_MCQ)(os.path.join(root_path, "mcq.csv"))
    for column in COLUMNS_QBANK_MCQ:
        try:
            if column != "repeat": 
                df[column] = df[column].str.strip() 
            if column != "question" and column != "repeat":
                df[column] = df[column].str.lower()

        except:
            pass
    # df = df[df["repeat"] != 1]
    # df = df[df["repeat"] != 2]
    # df = df[df["repeat"] != 3]
    df["level"] = df["level"].replace(to_replace =SYNONYMS_LOW, 
                            value ="low")
    df["level"] = df["level"].replace(to_replace =SYNONYMS_MEDIUM, 
                            value ="medium")
    df["level"] = df["level"].replace(to_replace =SYNONYMS_HIGH, 
                            value ="high")
    df["topic"] = df["legend"].apply(f)
    write_csv(df,os.path.join(root_path, "objective.csv"))


    
df = read_csv_generic(COLUMNS_QBANK)(os.path.join(root_path, "qbank.csv"))
for column in COLUMNS_QBANK:  
    if column != "repeat": 
        df[column] = df[column].str.strip() 
    if column != "question" and column != "repeat":
        df[column] = df[column].str.lower()
        
# df = df[df["repeat"] != 1]
# df = df[df["repeat"] != 2]
# df = df[df["repeat"] != 3]
df["topic"] = df["legend"].apply(f)
df["level"] = df["level"].replace(to_replace =SYNONYMS_LOW, 
                            value ="low")
df["level"] = df["level"].replace(to_replace =SYNONYMS_MEDIUM, 
                        value ="medium")
df["level"] = df["level"].replace(to_replace =SYNONYMS_HIGH, 
                        value ="high")
write_csv(df,os.path.join(root_path, "subjective.csv"))