from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

templateData = {
    'temp' : None,
    'humd' : None,
    'pressure' : None
}

@app.route('/', methods=['GET', 'PUT'])
def hello():
    error = None
    if request.method == 'PUT':

        data = json.loads(request.body.raw)

        templateData['temp'] = data['temp']
        templateData['humd'] = data['humd']
        templateData['pressure'] = data['pressure']

    else:
        return render_template('main.html', **templateData)


if __name__ == '__main__':
    app.run(port = 80, host = '127.0.0.1', debug = True)
