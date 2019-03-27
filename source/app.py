from flask import Flask, request, jsonify
from get_csv import *

app = Flask(__name__)

@app.route("/breakup/<path:uri>", methods = ['GET'])
def fetch_breakup(uri):
    location = uri.split('/')
    df, response_code = get_breakup(location[0], location[1], location[2])
    if response_code == 404:
        return 'no such file', 404
    return df_to_json(df), 201
    
@app.route("/legend/<path:uri>", methods = ['GET'])
def fetch_legend(uri):
    location = uri.split('/')
    df, response_code = get_legend(location[0], location[1], location[2])
    if response_code == 404:
        return 'no such file', 404
    return df_to_json(df), 201
    
@app.route("/paperConfig/<path:uri>", methods = ['GET'])
def fetch_paperConfig(uri):
    location = uri.split('/')
    df, response_code = get_paperConfig(location[0], location[1], location[2])
    if response_code == 404:
        return 'no such file', 404
    return df_to_json(df), 201
    

@app.route("/qBank/<path:uri>", methods = ['GET'])
def fetch_qBank(uri):
    location = uri.split('/')
    df, response_code = get_qBank(location[0], location[1], location[2])
    if response_code == 404:
        return 'no such file', 404
    return df_to_json(df), 201
    

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
