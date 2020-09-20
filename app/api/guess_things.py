from flask import jsonify, abort, request
from . import api

word_list = {
    'en_US': [
        'queen', 'hospital', 'basketball', 'cat', 'change', 'snail', 'soup',
        'calendar', 'sad', 'desk', 'guitar', 'home', 'railway', 'zebra',
        'jelly', 'car', 'crow', 'trade', 'bag', 'roll', 'bubble'
    ],
    'pt_BR': [
        'rainha', 'hospital', 'basquetebol', 'gato', 'mudança', 'caracol',
        'sopa', 'calendário', 'triste', 'escrivaninha', 'violão', 'casa',
        'estrada de ferro', 'zebra', 'geléia', 'carro', 'corvo', 'comércio',
        'bolsa', 'lista', 'bolha'
    ]
}


@api.route('/guess_things', methods=['GET'])
def get():
    if 'locale' not in request.args:
        abort(400, description='Locale must be provided')
    locale = request.args.get('locale')
    if locale not in word_list:
        abort(400, description='Locale not supported')
    words = word_list.get(locale)
    return jsonify({'things': words})
