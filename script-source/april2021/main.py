import os
from constants import *
def get_path(paper_type="cbme",  dept="anatomy", paper="paper1"):
     root_path = f"{paper_type}/{dept}/{paper}"
     return root_path

def generate(paper_type="cbme", dept="anatomy", paper="paper1", is_mcq = True, is_with_options=False):
     path=get_path(paper_type, dept, paper)
     config =  read_csv_generic(["key", "value"])(os.path.join(path, "format.csv"))
     qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(path, "subjective.csv"))
     mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(path, "objective.csv"))
     topic_split = {}
     if is_mcq:
          topic_split= topic
     p = PaperWithMCQ(topic_split, difficulty_split, qbank, mcqbank.copy())   
     p.build()
     p.q_bag.to_csv(os.path.join(path, 'paper.csv'), index=False)

def generate(path, is_mcq = True, is_with_options=False):
     # path=get_path(paper_type, dept, paper)
     config =  read_csv_generic(["key", "value"])(os.path.join(path, "format.csv"))
     qbank = read_csv_generic(COLUMNS_SUBJECTIVE)(os.path.join(path, "subjective.csv"))
     mcqbank = read_csv_generic(COLUMNS_OBJECTIVE)(os.path.join(path, "objective.csv"))
     topic_split = {}
     if is_mcq:
          topic_split= topic
     p = PaperWithMCQ(topic_split, difficulty_split, qbank, mcqbank)   
     p.build()
     p.q_bag.to_csv(os.path.join(path, 'paper.csv'), index=False)



     

if __name__=="__main__":
    path = sys.argv[1]
