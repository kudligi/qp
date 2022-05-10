import pandas as pd
from constants import *
from util import *
import sys
import os
from new_paper import *
import numpy as np

def f(x):
    return ''.join(filter(lambda i: i.isdigit(), x))

def f2(x):
    res = []
    for j in x[0]:
        res.append(''.join(filter(lambda i: i.isdigit(), j)))
    return [tuple(res), x[1]]

root_path=sys.argv[1]
# print(root_path)
# if "cbme" in root_path:
#     print(os.path.join(root_path, "mcq.csv"))
#     # MCQ QBANK:

#     df = read_csv_generic(COLUMNS_QBANK_MCQ)(os.path.join(root_path, "mcq.csv"))
#     for i in SYNONYMS_LOW:
#         df["level"] = df["level"].replace(i, "low")
#     for i in SYNONYMS_MEDIUM:
#         df["level"] = df["level"].replace(i, "medium")
#     for i in SYNONYMS_HIGH:
#         df["level"] = df["level"].replace(i, "high")
#     for column in COLUMNS_QBANK_MCQ:
#         if column != "repeat": 
#             df[column] = df[column].str.strip() 
#         if column != "question" and column != "repeat":
#             df[column] = df[column].str.lower()
#     # df["topic"] = ''.join(filter(lambda i: i.isdigit(), df["legend"].str))
#     df["topic"] = df["legend"].apply(f)
#     print(df.head())
#     write_csv(df,os.path.join(root_path, "objective.csv"))


# # QBANK:
# df = read_csv_generic(COLUMNS_QBANK)(os.path.join(root_path, "qbank.csv"))
# for i in SYNONYMS_LOW:
#     df["level"] = df["level"].replace(i, "low")
# for i in SYNONYMS_MEDIUM:
#     df["level"] = df["level"].replace(i, "medium")
# for i in SYNONYMS_HIGH:
#     df["level"] = df["level"].replace(i, "high")
# for column in COLUMNS_QBANK:   
#     if column != "repeat": 
#         df[column] = df[column].str.strip() 
#     if column != "question" and column != "repeat":
#         df[column] = df[column].str.lower()
# df["topic"] = df["legend"].apply(f)
# print(df.head())
# write_csv(df,os.path.join(root_path, "subjective.csv"))


#breakup:
df1 = read_csv_generic(["topic", "weight"])(os.path.join(root_path, "breakup.csv"))
df2 = read_csv_generic(["code", "topic", "sub"])(os.path.join(root_path, "legend.csv"))
df1["topic"] = df1["topic"].str.lower()
df2["topic"] = df2["topic"].str.lower()
topics = list(df1["topic"])
topics = [x.split('/') for x in topics] 
topics = [topic for x in topics for topic in x]

breakup_list = []
for index, row in df1.iterrows():
    temp = [df2[df2["topic"]==x]["code"].iloc[0] for x in row["topic"].split('/')] 
    # print(temp)
    breakup_list.append([tuple(temp), row["weight"]])


# print(root_path)
# print(breakup_list)

print(root_path)
if "cbme" in root_path:
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)("subjective.csv")
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)("objective.csv")
    p = PaperWithMCQ(breakup_list, difficulty_split, qbank, mcqbank, type_split_mcq)   
    p.build()
    p.q_bag.to_csv(os.path.join(root_path, "paperMCQ.csv"), index=False)

else:
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)("subjective.csv")
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)("subjective.csv")
    p = PaperWithMCQ(breakup_list, difficulty_split, qbank, mcqbank, type_split_no_mcq)   
    p.build()
    p.q_bag.to_csv(os.path.join(root_path, "paperNM.csv"), index=False)


    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)("subjective.csv")
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)("subjective.csv")
    p = PaperWithMCQ(breakup_list, difficulty_split, qbank, mcqbank, type_split_no_mcq_with_options)   
    p.build()
    p.q_bag.to_csv(os.path.join(root_path, "paperNMWO.csv"), index=False)
    


# for topic in topics:
#     if topic not in list(df2["topic"]):
#         print("Big Trouble ", topic, root_path)
#     else:
#         # print("A OK ", topic, root_path)
#         pass
    
