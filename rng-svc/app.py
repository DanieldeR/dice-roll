from flask import Flask
from random import choices

app = Flask(__name__)

def get_rng():
    dice_array = range(1, 7)

    data = choices(dice_array, k=10)

    return data

@app.route('/')
def hello():
    data = get_rng()

    return {"rngs": data}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')