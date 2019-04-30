from gevent import monkey; monkey.patch_all()
import bottle
from bottle import route, run, response, get, post, request, install
import json
import requests

#Enable Cors to send/recieve data.
class EnableCors(object):
    name = 'enable_cors'
    api = 2
    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
            if bottle.request.method != 'OPTIONS':
                return fn(*args, **kwargs)
        return _enable_cors

@post('/logging')
def logger():
    body = request.json
    print(body)
    f = open('results.log','a+')
    f.write(str(body) + "\n")
    f.close()

install(EnableCors())
run(host='0.0.0.0', port=3000, debug=True, server='gevent')
