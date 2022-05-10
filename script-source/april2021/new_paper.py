import pandas as pd
from constants import *
from util import *
import os
import sys
import traceback
from word import *

def f(x):
    return ''.join(filter(lambda i: i.isdigit(), x))


class PaperWithMCQ:

    def __init__(self, topic_split, difficulty_split, qbank, mcq_bank, type_split, is_mcq):
        self.q_bag = pd.DataFrame(columns = ["question", "marks", "topic", "sub_topic", "level", "type"])
        self.q_counters_down = {a:b for a, b in type_split}
        self.topic_split_down = {a:b for a, b in topic_split}
        self.difficulty_split_down = difficulty_split.copy()
        self.qbank_reference = qbank
        self.scratch_bank = qbank.copy()
        self.scratch_bank["mask"] = 0
        self.mcq_bank_refernce = mcq_bank
        self.scratch_mcq_bank = mcq_bank.copy()
        self.le_preferred_topics = le_preferred_topics
        self.is_mcq = is_mcq

    def pick_le_questions(self):
        count = self.q_counters_down["le"]
        df = filter_by_equality("type", "le")(self.scratch_bank)

        self.scratch2 = df.copy()
        
        # df = filter_by_list_of_values(self.le_preferred_topics, df, "topic")
        self.scratch1 = df.copy()
        self.filter_difficulty_cutoffs(10)

        for i in range(count):
            try:
                row, df = pick_question(self.scratch1)
            except:
                row, df = pick_question(self.scratch2)
            
            self.scratch2 = filter_by_inequality("legend", row['legend'].iloc[0])(df)
            self.scratch1 = filter_by_inequality("topic", row['topic'].iloc[0])(df)

            question = {
                "question" : row["question"].iloc[0], 
                "marks" : TYPE2MARKS[row["type"].iloc[0]], 
                "topic" : row["topic"].iloc[0], 
                "sub_topic" : row["legend"].iloc[0], 
                "level" : row["level"].iloc[0], 
                "type" : row["type"].iloc[0]
                # ,
                # "repeat" : row["repeat"].iloc[0]
            }

            self.q_bag = self.q_bag.append(question, ignore_index=True)
            self.q_counters_down["le"] -= 1

            for topics in self.topic_split_down:
                if row["topic"].iloc[0] in topics:
                    self.topic_split_down[topics] = self.topic_split_down[topics] - TYPE2MARKS["le"]
                    break
            # print(row["level"].iloc[0])

            self.difficulty_split_down[row["level"].iloc[0]] = self.difficulty_split_down[row["level"].iloc[0]] - TYPE2MARKS["le"]

            # print(self.q_counters_down)
            # print(self.topic_split_down)

    def pick_questions(self, type):
        count = self.q_counters_down[type]
        if type != 'mcq': df = filter_by_equality("type", type)(self.scratch_bank)
        else: df = filter_by_equality("type", type)(self.scratch_mcq_bank)
        self.scratch4 = df.copy()
        self.scratch3 = df.copy()
        self.scratch2 = df.copy()
        self.scratch1 = df.copy()
        self.filter_topics_in_split()
        
        for i in range(count):
            # print(type, i)
            try:
                row, df2 = pick_question(self.scratch1)
            except:
                try:
                    row, df2 = pick_question(self.scratch2)
                    self.scratch1 = self.scratch2.copy()
                except:
                    try:
                        row, df2 = pick_question(self.scratch3)
                        self.scratch2 = self.scratch3.copy()
                        self.scratch1 = self.scratch3.copy()
                    except: 
                        try:
                            row, df2 = pick_question(self.scratch4)
                            self.scratch3 = self.scratch4.copy()
                            self.scratch2 = self.scratch4.copy()
                            self.scratch1 = self.scratch4.copy()
                        except:
                            print(df)
                            print(self.scratch1)
                            # print(self.scratch2)
                            # print(self.scratch3)
                            # print(self.scratch4)
                            # exit()
                            pass

           
            self.scratch2 = filter_by_inequality("legend", row['legend'].iloc[0])(self.scratch2)
            self.scratch2 = filter_by_inequality("legend", row['legend'].iloc[0])(self.scratch2)
            self.scratch1 = filter_by_inequality("topic", row['topic'].iloc[0])(self.scratch1)
            
            question = {
                "question" : row["question"].iloc[0], 
                "marks" : TYPE2MARKS[row["type"].iloc[0]], 
                "topic" : row["topic"].iloc[0], 
                "sub_topic" : row["legend"].iloc[0], 
                "level" : row["level"].iloc[0], 
                "type" : row["type"].iloc[0]
                # ,
                # "repeat" : row["repeat"].iloc[0]
            }

            if type == "mcq":
                question["option1"] = row["option1"].iloc[0]                 
                question["option2"] = row["option2"].iloc[0]             
                question["option3"] = row["option3"].iloc[0]             
                question["option4"] = row["option4"].iloc[0]     

            else:
                question["option1"] = "no options"                 
                question["option2"] = "no options"             
                question["option3"] = "no options"             
                question["option4"] = "no options"     
                        

            self.q_bag = self.q_bag.append(question, ignore_index=True)
            self.q_counters_down[type] -= 1
            for topics in self.topic_split_down:
                if row["topic"].iloc[0] in topics:
                    self.topic_split_down[topics] = self.topic_split_down[topics] - TYPE2MARKS["mcq"]
                    break
            self.difficulty_split_down[row["level"].iloc[0]] = self.difficulty_split_down[row["level"].iloc[0]] - TYPE2MARKS["mcq"]
            # print(self.q_counters_down)
        
    def filter_difficulty_cutoffs(self, threshold):
        for level in self.difficulty_split_down:
            if self.difficulty_split_down[level] < threshold:
                try:
                    self.scratch1 = filter_by_inequality("level", level)(self.scratch1)
                    self.scratch2 = filter_by_inequality("level", level)(self.scratch2)
                    self.scratch3 = filter_by_inequality("level", level)(self.scratch3)
                    self.scratch4 = filter_by_inequality("level", level)(self.scratch4)
                except:
                    pass


    def filter_breakup_cutoffs(self, threshold):
        for topics in self.topic_split_down:
            if self.topic_split_down[topics] <= threshold:
                for topic in topics:
                    self.scratch1 = filter_by_inequality("topic", topic)(self.scratch1)
                    self.scratch2 = filter_by_inequality("topic", topic)(self.scratch2)
                    self.scratch3 = filter_by_inequality("topic", topic)(self.scratch3)
                    self.scratch4 = filter_by_inequality("topic", topic)(self.scratch4)

    def filter_topics_in_split(self):
        res = []
        for topics in self.topic_split_down:
            for topic in topics:
                res.append(int(topic))
        # print("filtering", res)
        self.scratch4 = filter_by_list_of_values(res, self.scratch4, "topic")
        self.scratch3 = filter_by_list_of_values(res, self.scratch3, "topic")
        self.scratch2 = filter_by_list_of_values(res, self.scratch2, "topic")
        self.scratch1 = filter_by_list_of_values(res, self.scratch1, "topic")
        
        

    def build(self):
        self.pick_le_questions()
        self.pick_questions("se")
        self.pick_questions("sa")
        if self.is_mcq:
            self.pick_questions("mcq")

    def stats(self):
        topic_summary = self.q_bag.groupby('topic').agg(
            {
                'marks':sum
            }
        )
        difficulty_summary = self.q_bag.groupby('level').agg(
            {
                'marks':sum
            }
        )
        return topic_summary, difficulty_summary


def f2(x):
    res = []
    for j in x[0]:
        res.append(''.join(filter(lambda i: i.isdigit(), j)))
    return [tuple(res), x[1]]



if __name__=="__main__":
    # for i in range(5):
    #     root_path="./data/cbme/physiology/paper1"
    #     qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
    #     mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "objective.csv"))
    #     p = PaperWithMCQ(topic_split, {
    #         "low": 60,
    #         "medium": 30,
    #         "high": 10
    #     }, qbank, mcqbank.copy(), type_split_mcq)   
    #     p.build()
    #     p.q_bag.to_csv(f'paper{i}.csv', index=False)
    #     a, b = p.stats()
    #     print("Distribution of topics",a, topic_split)
    #     print("Distribution of difficulty",b, difficulty_split)
    root_path=sys.argv[1]
    




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
    


    if "cbme" in root_path:
        qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
        mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "objective.csv"))
        p = PaperWithMCQ(breakup_list, {
            "low": 60,
            "medium": 30,
            "high": 10
        }, qbank, mcqbank.copy(), type_split_mcq, True)   
    else:
        qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(root_path, "subjective.csv"))
        mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(root_path, "subjective.csv"))
        p = PaperWithMCQ(breakup_list, {
            "low": 60,
            "medium": 30,
            "high": 10
        }, qbank, mcqbank.copy(), type_split_mcq, False)
    try:
        p.build()
        print(root_path, "oooooooooooo")
    except:
        print(root_path, "XXXXXXXXX")
        traceback.print_exception(*sys.exc_info())
        exit()

    p.q_bag.to_csv(os.path.join(root_path, "paper.csv"), index=False)
    a, b = p.stats()

    config = util.read_csv_python(os.path.join(root_path, "format.csv"), ["key", "value"])
    config_dict = pd.Series(config.value.values,index=config.key.values).to_dict()
    if "cbme" in root_path:
        document = Document()
        document1 = make_header(document, config_dict, True)
        document2 = make_paper(document1, p.q_bag)
        document.save(os.path.join(root_path, "paper.docx"))
        document = Document()
        document1 = make_header(document, config_dict, True)
        document2 = make_paper(document1, p.q_bag)
        document.save(os.path.join(root_path, "paperMCQ.docx"))

    else:
        document = Document()
        document1 = make_header(document, config_dict, False)
        document2 = make_paper(document1, p.q_bag)
        document.save(os.path.join(root_path, "paper.docx"))
        document = Document()
    # print("Distribution of topics",a, topic_split)
    # print("Distribution of difficulty",b, difficulty_split)