import pandas as pd
from constants import *
from util import *
import sys
import os

def f(x):
    return ''.join(filter(lambda i: i.isdigit(), x))

root_path=sys.argv[1]


# QBANK:
df = read_csv_generic(COLUMNS_QBANK)(os.path.join(root_path, "qbank.csv"))
for column in COLUMNS_QBANK:
    if column != "repeat": 
        df[column] = df[column].str.strip() 
    if column != "question":
        df[column] = df[column].str.lower()
df["topic"] = df["legend"].apply(f)
print(df.head())
write_csv(df,os.path.join(root_path, "subjective.csv"))