from flask import Flask, request, jsonify
import json
from get_csv import *
import os
from metadata import *
import requests

app = Flask(__name__)

logCount = 0

def callPostLog(messageData, callName):
    r = requests.post(url='http://localost:3000/' + callName, data=messageData)
    #print(r.status_code, r.reason, r.text)

def log(tag, method, aiText, mess):
    logCount += 1
    messageData = {"index":{"index":"qp", "_id": logCount}, "level": "info", "message":""}
    messageData2 = {"type": "api_call", "call_name": tag, "method" : method, "text_entry": aiText, "sender_id" : 'admin', "level": "info", "message": mess}
    callPostLog(messageData, 'log')
    callPostLog(messageData2, 'logging')

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
    log('metadata/course_list', 'GET', '201', "")
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
