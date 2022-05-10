import pandas as pd
from constants import *

def read_csv_python(path, names):
    return pd.read_csv(path, names=names, index_col=False, engine='python')

def read_csv_c(path, names):
    return pd.read_csv(path, names=names, index_col=False)


read_csv_generic_c = lambda names: lambda path: read_csv_c(path, names).dropna()
read_csv_generic = lambda names: lambda path: read_csv_python(path, names).dropna()
read_csv_generic_without_drop = lambda names: lambda path: read_csv_python(path, names)

def write_csv(df, path):
    df.to_csv(path, header=False, index=False)

filter_by_equality = lambda column, value: lambda df: df[df[column] == value]
filter_by_contains = lambda column, value: lambda df: df[df[column].str.contains(value)]
filter_by_inequality = lambda column, value: lambda df: df[df[column] != value]
filter_by_greater_than = lambda column, value: lambda df: df[df[column] > value]

mask_filter = lambda legend: filter_by_inequality("legend", legend)

add_topicbias_to_mask = lambda topic: lambda df, bias: df[df["topic"] == topic]["mask"] + bias

def filter_by_list_of_values(topics, df, column):
    res = []
    for topic in topics:
        res.append(filter_by_equality(column, topic)(df))
    return pd.concat(res)


set_difference = lambda df1, df2:  pd.concat([df2, df1, df1]).drop_duplicates(keep=False)

def pick_question(df):
    row =  df.sample(n=1)
    new_df = set_difference(row, df)
    return row, new_df


if __name__ == "__main__":
    df = read_csv_generic(COLUMNS_QBANK_MCQ)("qbank_mcq.csv")
    df = df.head(10)
    # print(df)
    row, df2 = pick_question(df)
    df3 = filter_by_inequality("legend", row["legend"].iloc[0])(df2)
    print(row["question"])
    print(df2["question"])
    print(df3["question"])



# read_qbank_mcq = read_csv_generic(COLUMNS_QBANK_MCQ)
# read_format = read_csv_generic(COLUMNS_FORMAT)
# read_qbank = read_csv_generic(COLUMNS_QBANK)

# df = read_qbank("qbank.csv")
# # df = read_format("format.csv")

# filter_df_by = lambda filter: lambda df: filter(df)



# filter_qbank_level_easy = filter_by_equality("level", "EASY")
# filter_qbank_level_medium = filter_by_equality("level", "MEDIUM")
# filter_qbank_level_high = filter_by_equality("level", "HIGH")


# filter_qbank_level_easy = filter_df_by(lambda df: df[df["level"] == "EASY"])
# filter_qbank_level_medium = filter_df_by(lambda df: df[df["level"] == "MEDIUM"])
# filter_qbank_level_high = filter_df_by(lambda df: df[df["level"] == "HIGH"])

#QESTIONS,OPTION -1,OPTION -2,OPTION -3,OPTION -4,LEGENDS,Level
# df = read_csv("qbank.csv", ["questions", "option1", "option2", "option3", "option4", "legend", "level"])
# print(df.head())
# print(df.columns)

# for i in range(1,7):
#     print(filter_by_contains("legend", str(i))(df).size)