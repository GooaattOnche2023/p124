import flask
from flask import Flask, jsonify
app= Flask(_name_)
{   
    'data':[
        {
            'Contact':'24323453',
            'Name':'Tim',
            'done': False,
            'id': 1
        },
        {
            'Contact':'24823453',
            'Name':'Tommy',
            'done': False,
            'id': 2
        }
    ]
}

@app.route('/app-data', methods=['POST'])

def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the data'
        },400)

contact = {
    'id': task[-1]['id'] +1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact',''),
    'done':False
}