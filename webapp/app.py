from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

am_i_in_docker = os.environ.get('AM_I_IN_DOCKER', 'no')

if am_i_in_docker == 'yes':
    rng_url = "http://rng-svc:5000"
else: 
    rng_url = "http://127.0.0.1:5000"

@app.route('/')
def hello():
    data = requests.get(rng_url).json()

    return render_template('index.html', data=data['rngs'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)