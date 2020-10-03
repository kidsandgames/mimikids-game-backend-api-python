from flask import jsonify, abort, request
from . import api

word_list = {
    'en': {
        'animals': [
            'whale', 'dog', 'horse', 'snake', 'rabbit', 'crocodile',
            'elephant', 'chicken', 'cat', 'dolphin', 'lion', 'giraffe', 'wolf',
            'monkey', 'parrot', 'rat', 'turtle', 'bear', 'cow'
        ],
        'objects': [
            'fan', 'broom', 'table', 'clock', 'phone', 'whiteboard',
            'baby carriage', 'glass of water', 'cup of tea', 'bicycle',
            'bucket', 'computer', 'cell phone', 'mouse', 'chair', 'trash can',
            'typewriter', 'stapler'
        ],
        'emotions': [
            'joy', 'anxiety', 'apathy', 'depression', 'pain', 'doubt',
            'ecstasy', 'envy', 'hunger', 'frustration', 'horror', 'fear',
            'hatred', 'pride', 'anger', 'surprise', 'boredom', 'sadness'
        ]
    },
    'pt_BR': {
        'animals': [
            'baleia', 'cachorro', 'cavalo', 'cobra', 'coelho', 'crocodilo',
            'elefante', 'galinha', 'gato', 'golfinho', 'leão', 'girafa',
            'lobo', 'macaco', 'papagaio', 'rato', 'tartaruga', 'urso', 'vaca'
        ],
        'objects': [
            'ventilador', 'vassoura', 'mesa', 'relógio', 'telefone',
            'quadro branco', 'carrinho de bebê', 'copo de água',
            'xícara de chá', 'bicicleta', 'balde', 'computador', 'celular',
            'mouse', 'cadeira', 'lixeira', 'máquina de escrever', 'grampeador'
        ],
        'emotions': [
            'alegria', 'ansiedade', 'apatia', 'depressão', 'dor', 'dúvida',
            'êxtase', 'inveja', 'fome', 'frustração', 'horror', 'medo', 'ódio',
            'orgulho', 'raiva', 'surpresa', 'tédio', 'tristeza'
        ]
    }
}


@api.route('/guess/<category>', methods=['GET'])
def get(category):
    if 'locale' not in request.args:
        abort(400, description='Locale must be provided')
    locale = request.args.get('locale')
    if locale not in word_list:
        abort(400, description='Locale not supported')
    if category not in word_list[locale]:
        abort(404, description=f'Category {category} doesn\'t exists')
    words = word_list[locale][category]
    return jsonify({category: words})
