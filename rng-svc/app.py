from flask import Flask
from random import choices
import itertools

app = Flask(__name__)

card_array = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit_array = ['C', 'H', 'S', 'D']

deck = [f'{a}{b}' for a, b in itertools.product(card_array, suit_array)]

def get_rng():

    data = choices(deck, k=5)

    return data

@app.route('/')
def hello():
    data = get_rng()

    return {"rngs": data}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')