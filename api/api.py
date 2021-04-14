import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"api/*":{"origins":"*"}})
app.config['CORS HEADERS'] = 'Content-Type'



@app.route('/api/search_query', methods = ['GET', 'POST'])
@cross_origin()
def get_search_query(): 
    data = request.get_json()
    return {'query': data}

    




