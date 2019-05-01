from flask import Flask, request, jsonify
import json
from get_csv import *
import os
from metadata import *
import requests
from elasticsearch import Elasticsearch 

app = Flask(__name__)
'''
global logCount
logCount = 0
es = Elasticsearch([{'host': 'localhost', 'port' : 9200 }])

@app.route("/log", methods = ['GET'])
def log(tag, method, status, mess):
    global logCount
    logCount += 1
    message = {'endpoint' : tag, 'method' : method, 'status' : status, 'uri' : mess}
    es.index(index='lol', doc_type='troll', id = logCount, body=message)
    
'''

def log(tag, method, status, mess):
    requests.get('https://80cbe497.ngrok.io/log/'+str(tag.replace('/','_'))+'/' +str(method).replace('/','_')+'/'+str(status).replace('/','_')+'/'+str(mess).replace('/','_'))
    

@app.route("/breakup/<path:uri>", methods = ['GET'])
def fetch_breakup(uri):
    location = uri.split('/')
    df, response_code = get_breakup(location[0], location[1], location[2])
    if response_code == 404:
        log('breakup', 'GET', '404', uri)
        return 'no such file', 404
    log('breakup', 'GET', '201', uri)
    return df_to_json(df), 201
    
@app.route("/legend/<path:uri>", methods = ['GET'])
def fetch_legend(uri):
    location = uri.split('/')
    df, response_code = get_legend(location[0], location[1], location[2])
    if response_code == 404:
        log('legend', 'GET', '404', uri)
        return 'no such file', 404
    log('legend', 'GET', '201', uri)
    return df_to_json(df), 201
    
@app.route("/paperConfig/<path:uri>", methods = ['GET'])
def fetch_paperConfig(uri):
    location = uri.split('/')
    df, response_code = get_paperConfig(location[0], location[1], location[2])
    if response_code == 404:
        log('paperConfig', 'GET', '404', uri)
        return 'no such file', 404
    log('paperConfig', 'GET', '201', uri)
    return df_to_json(df), 201
    

@app.route("/qBank/<path:uri>", methods = ['GET'])
def fetch_qBank(uri):
    location = uri.split('/')
    df, response_code = get_qBank(location[0], location[1], location[2])
    if response_code == 404:
        log('qBank', 'GET', '404', uri)
        return 'no such file', 404
    log('qBank', 'GET', '201', uri)
    return df_to_json(df), 201



@app.route("/metadata/course_list", methods = ['GET'])
def get_clist():
    log('metadata/course_list', 'GET', '201', "xxx")
    return jsonify(get_course_list())



@app.route("/metadata/departments_list/<string:course>", methods = ['GET'])
def get_dlist(course):
    log('metadata/departments_list', 'GET', '201', course)
    return jsonify(get_departments_list(course))



@app.route("/metadata/papers_list/<string:course>/<string:department>", methods = ['GET'])
def get_plist(course,department):
    log('metadata/papers_list', 'GET', '201', course + '/' + department)
    return jsonify(get_papers_list(course,department))



@app.route("/breakup/<path:uri>", methods = ['POST'])
def set_breakup(uri):
    path = './data/' + uri + '/breakup.csv'
    j = request.json
    df = pd.read_json(json.dumps(j),  orient = 'records')
    df.to_csv(path, index = False)
    log('breakup', 'POST', '201', uri)
    return json.dumps(j), 201

@app.route("/legend/<path:uri>", methods = ['POST'])
def set_legend(uri):
    path = './data/' + uri + '/legend.csv'
    j = request.json
    df = pd.read_json(json.dumps(j),  orient = 'records')
    df.to_csv(path, index = False)
    log('legend', 'POST', '201', uri)
    return json.dumps(j), 201

@app.route("/paperConfig/<path:uri>", methods = ['POST'])
def set_paperConfig(uri):
    path = './data/' + uri + '/paperConfig.csv'
    j = request.json
    df = pd.read_json(json.dumps(j),  orient = 'records')
    df.to_csv(path, index = False)
    log('paperConfig', 'POST', '201', uri)
    return json.dumps(j), 201

@app.route("/qBank/<path:uri>", methods = ['POST'])
def set_qBank(uri):
    path = './data/' + uri + '/qBank.csv'
    j = request.json
    df = pd.read_json(json.dumps(j),  orient = 'records')
    df.to_csv(path, index = False)
    log('qbank', 'POST', '201', uri)
    return json.dumps(j), 201



















'''

@app.route("/ls1", methods = ['GET'])
def show():
    a = commands.getoutput('ls ../')
    return a


@app.route("/ls2", methods = ['GET'])
def show2():
    a = commands.getoutput('ls')
    return a


@app.route("/ls3", methods = ['GET'])
def show3():
    a = commands.getoutput('ls ../app/')
    return a


@app.route("/ls4", methods = ['GET'])
def show4():
    a = commands.getoutput('ls ./data/')
    return a

'''

if __name__ == '__main__':
    #print(os.system('ls ../'))
    app.run(debug=True, port = 5000)
