import pandas as pd
import sys
import os
from constants import *
from util import *
from new_paper import *


check_folder_exists = lambda folder: lambda dept: lambda paper: dept in os.listdir(os.path.join("data", folder)) and paper in os.listdir(os.path.join("data", folder, dept))

def get_breakup(root_path):
    df1 = read_csv_generic(["topic", "weight"])(os.path.join(root_path, "breakup.csv"))
    df2 = read_csv_generic(["code", "topic", "sub"])(os.path.join(root_path, "legend.csv"))
    df1["topic"] = df1["topic"].str.lower()
    df2["topic"] = df2["topic"].str.lower()
    topics = list(df1["topic"])
    topics = [x.split('/') for x in topics] 
    topics = [topic for x in topics for topic in x]

    breakup_list = []
    for index, row in df1.iterrows():
        # print("YYYYY")\
        try:
            temp = [df2[df2["topic"]==x]["code"].iloc[0] for x in row["topic"].split('/')] 
        except:
            print(row["topic"])
        # print(temp)
        breakup_list.append([tuple(temp), row["weight"]])



    breakup_list = [f2(x) for x in breakup_list]
    return breakup_list


timetable = pd.read_csv("timetable.csv")

print(timetable)

date = sys.argv[1]
session = sys.argv[2]

df = timetable[timetable["date"]==date]


print(df)
### morning session
try:
    morning = df[session].iloc[0]
except:
    print("incorrect date please check timetable.csv")
    exit()
morning_dept = morning.split("-")[0]
morning_paper = morning.split("-")[1]

print(check_folder_exists("cbme")(morning_dept)("paper"+morning_paper))
if check_folder_exists("cbme")(morning_dept)("paper"+morning_paper):
    root_path=os.path.join("data/cbme", morning_dept, "paper"+morning_paper)
    config = util.read_csv_python(os.path.join(root_path, "format.csv"), ["key", "value"])
    config_dict = pd.Series(config.value.values,index=config.key.values).to_dict()
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "objective.csv"))
    breakup_list = get_breakup(root_path)
    p = PaperWithMCQ(breakup_list, {
            "low": 60,
            "medium": 30,
            "high": 10
        }, qbank, mcqbank.copy(), type_split_mcq, True)
    p.build()
    a, b = p.stats()
    document = Document()
    document1 = make_header(document, config_dict, False)
    document2 = make_paper(document1, p.q_bag)
    document.save(os.path.join("papers", f"{morning}-subjective80.docx"))
    document = Document()
    document1 = make_header(document, config_dict, True)
    document2 = make_mcq_paper(document1, p.q_bag)
    document.save(os.path.join("papers", f"{morning}-mcq20.docx"))

    print(morning)
    print(a)
    print(b)


if check_folder_exists("old_pattern")(morning_dept)("paper"+morning_paper):
    root_path=os.path.join("data/old_pattern", morning_dept, "paper"+morning_paper)
    config = util.read_csv_python(os.path.join(root_path, "format.csv"), ["key", "value"])
    config_dict = pd.Series(config.value.values,index=config.key.values).to_dict()
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    breakup_list = get_breakup(root_path)
    p = PaperWithMCQ(breakup_list, {
            "low": 60,
            "medium": 30,
            "high": 10
        }, qbank, mcqbank.copy(), type_split_no_mcq, False)
    p.build()
    a, b = p.stats()

    print(morning)
    print(a)
    print(b)

    document = Document()
    document1 = make_header(document, config_dict, False)
    document2 = make_paper(document1, p.q_bag)
    document.save(os.path.join("papers", f"{morning}-subjective100.docx"))
    document = Document()

    p = PaperWithMCQ(breakup_list, {
            "low": 60,
            "medium": 30,
            "high": 10
        }, qbank, mcqbank.copy(), type_split_no_mcq_with_options, False)
    p.build()
    a, b = p.stats()
    document = Document()
    document1 = make_header(document, config_dict, False)
    document2 = make_paper(document1, p.q_bag, False, True)
    document.save(os.path.join("papers", f"{morning}-subjective100options.docx"))
    document = Document()
    
    print(morning)
    print(a)
    print(b)


if morning_dept=="surg+ortho":
    root_path=os.path.join("data/special/surg+ortho/ortho1")
    config = util.read_csv_python(os.path.join(root_path, "format.csv"), ["key", "value"])
    config_dict = pd.Series(config.value.values,index=config.key.values).to_dict()
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    breakup_list = get_breakup(root_path)
    p = PaperWithMCQ(breakup_list, {
            "low": 30,
            "medium": 15,
            "high": 5
        }, qbank, mcqbank.copy(), type_split_half, False)
    p.build()
    a, b = p.stats()

    print(morning)
    print(a)
    print(b)

    document = Document()
    document1 = make_header(document, config_dict, False, True)
    document2 = make_paper(document1, p.q_bag, False, False, True)
    # document.save(os.path.join("papers", f"ortho1-half.docx"))
    
    root_path=os.path.join("data/special/surg+ortho/surgery1")
    config = util.read_csv_python(os.path.join(root_path, "format.csv"), ["key", "value"])
    config_dict = pd.Series(config.value.values,index=config.key.values).to_dict()
    qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    breakup_list = get_breakup(root_path)
    p = PaperWithMCQ(breakup_list, {
            "low": 30,
            "medium": 15,
            "high": 5
        }, qbank, mcqbank.copy(), type_split_half, False)
    p.build()
    a, b = p.stats()

    print(morning)
    print(a)
    print(b)

    # document = Document()
    # document1 = make_header(document, config_dict, False)
    document4 = add_section(document2, config_dict["subject"])
    document3 = make_paper(document4, p.q_bag, False, False, True)
    # document.save(os.path.join("papers", f"surgery1-half.docx"))
    document.save(os.path.join("papers", f"surg+ortho1.docx"))
    


