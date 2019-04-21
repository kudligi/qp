from get_csv import *
from util import *
import numpy as np

def gen_paper(course, department, paper):
    
    
    qContrib = {'le': 0.1,
                'se': 0.05,
                'sa': 0.03}
    
    qCandidates = {
            'le': 2,
            'se': 10,
            'sa': 10}

    
    
    breakup_df = pd.read_csv('../data' + '/' + course + '/' + department + '/' + paper + '/breakup.csv', encoding='cp1252' )

    #TOPIC BREAKUP IN FRACTIONS
    topicBreakup = {}
    for a,b in breakup_df.iterrows():
        topicBreakup[b['topic']] = b['weightage'] / 100
    topicBreakup = OrderedDict(sorted(topicBreakup.items(), key = lambda t: t[1]))

    topicBreakup_cache = dict(topicBreakup)
    
    qBucketsWithoptions = fillBucketsWithOptions(topicBreakup, qContrib, qCandidates, topicBreakup, topicBreakup_cache)
    qBuckets =  fillBuckets(topicBreakup, qContrib, qCandidates, topicBreakup, topicBreakup_cache)

    legend_df = pd.read_csv('../data' + '/' + course + '/' + department + '/' + paper + '/legend.csv', encoding='cp1252' )
    qBank_df = pd.read_csv('../data' + '/' + course + '/' + department + '/' + paper + '/qBank.csv', encoding='cp1252' )

    blueprint_df = qBuckets
    blueprint_dfWithOptions = qBucketsWithoptions

    for column in blueprint_df:
        blueprint_df[column] = blueprint_df[column].str.lower()
        blueprint_df[column] = blueprint_df[column].str.strip()

    for column in blueprint_dfWithOptions:
        blueprint_dfWithOptions[column] = blueprint_dfWithOptions[column].str.lower()
        blueprint_dfWithOptions[column] = blueprint_dfWithOptions[column].str.strip()

    for column in qBank_df:
        if column != 'question':
            qBank_df[column] = qBank_df[column].str.lower()
            qBank_df[column] = qBank_df[column].str.strip() 

    for column in legend_df:
        legend_df[column] = legend_df[column].str.lower()
        legend_df[column] = legend_df[column].str.strip() 

    qdb_df = pd.merge(legend_df,qBank_df,on='code',how ='right')
    qdb_df = qdb_df.drop('code', axis = 1)
    qdb_df['mask'] = np.where(True,0,1)
    qdb_df['picked'] = np.where(True,0,1)
    blueprint_df['question'] = np.where(True,"no question matching constrains",1)
    blueprint_df['sub_topic'] = np.where(True,"no question matching constrains",1)  


    df = populateBluePrint(blueprint_df, qdb_df)

    blueprint_dfWithOptions['question'] = np.where(True,"no question matching constrains",1)
    blueprint_dfWithOptions['sub_topic'] = np.where(True,"no question matching constrains",1)
    
    dfWithOptions = populateBluePrint(blueprint_dfWithOptions, qdb_df)

    paperConfi = pd.read_csv('../data' + '/' + course + '/' + department + '/' + paper + '/paperConfig.csv', encoding='cp1252' )
    paperConfig = {}
    for k, v in paperConfi.iterrows():
        paperConfig[v['key']] = v['value']
    dfWithOptions = populateBluePrint(blueprint_dfWithOptions, qdb_df)
    setPaper_no_options(df, paperConfig, "apple")
    return "oh my god"
print(gen_paper('UG', 'forensic_medicine' , '113'))