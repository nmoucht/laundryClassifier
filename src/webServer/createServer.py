from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/getLaundryState', methods=('GET'))
def getState():
    data = {}
    data['washer'] = 'nikosm'
    data['drier'] = 'off'
    json_data = json.dumps(data)
    return json_data

if __name__ == '__main__':
   app.run()