import pandas as pd
import os
import sys
from constants import *
from util import *
from new_paper import *
import numpy as np

import traceback

def f(x):
    try:
        ''.join(filter(lambda i: i.isdigit(), x))
    except:
        print(f"@@@@@@@@{x}")
    return ''.join(filter(lambda i: i.isdigit(), x))

root_path=sys.argv[1]
print(root_path)
if "cbme" in root_path:
    print(os.path.join(root_path, "mcq.csv"))
    # MCQ QBANK:

    df = read_csv_generic_without_drop(COLUMNS_QBANK_MCQ_REPEATED)(os.path.join(root_path, "mcq.csv"))
    for column in COLUMNS_QBANK_MCQ:
        try:
            if column != "repeat": 
                df[column] = df[column].str.strip() 
            if column != "question" and column != "repeat":
                df[column] = df[column].str.lower()

        except:
            pass
    df["repeat"] = df["repeat"].fillna(0)
    df = df[df["repeat"] < 1 ]
    df = df.drop('repeat', 1)
    df["level"] = df["level"].replace(to_replace =SYNONYMS_LOW, 
                            value ="low")
    df["level"] = df["level"].replace(to_replace =SYNONYMS_MEDIUM, 
                            value ="medium")
    df["level"] = df["level"].replace(to_replace =SYNONYMS_HIGH, 
                            value ="high")
    try:
        df["topic"] = df["legend"].fillna("300-X").apply(f)
    except:
        print(df["legend"])
        print(root_path, "$$$$$")
        traceback.print_exception(*sys.exc_info())
        exit()

    write_csv(df,os.path.join(root_path, "objective.csv"))


    
df = read_csv_generic_without_drop(COLUMNS_QBANK_REPEATED)(os.path.join(root_path, "qbank.csv"))
for column in COLUMNS_QBANK:  
    if column != "repeat": 
        df[column] = df[column].str.strip() 
    if column != "question" and column != "repeat":
        df[column] = df[column].str.lower()
df["repeat"] = df["repeat"].fillna(0)        
df = df[df["repeat"] < 1 ]
df = df.drop('repeat', 1)
try:
    df["topic"] = df["legend"].fillna("300-X").apply(f)
except:
    print(df["legend"])
    print(root_path, "$$$$$")
    traceback.print_exception(*sys.exc_info())
    exit()
df["level"] = df["level"].replace(to_replace =SYNONYMS_LOW, 
                            value ="low")
df["level"] = df["level"].replace(to_replace =SYNONYMS_MEDIUM, 
                        value ="medium")
df["level"] = df["level"].replace(to_replace =SYNONYMS_HIGH, 
                        value ="high")
write_csv(df,os.path.join(root_path, "subjective.csv"))