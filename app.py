#from flask import Flask, request, jsonify
#from flask_cors import CORS
#import epitran
#
#app = Flask(__name__)
#CORS(app)  # Active CORS pour toutes les routes
#epi = epitran.Epitran('fra-Latn')
#
#@app.route('/getIPA', methods=['GET'])
#def get_ipa():
#    word = request.args.get('word')
#    if word:
#        phonemes = epi.transliterate(word)
#        return jsonify({'ipa': phonemes})
#    else:
#        return jsonify({'error': 'Aucun mot fourni'}), 400
#
#if __name__ == '__main__':
#    app.run(debug=True, port=5000)
#
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import epitran

app = Flask(__name__)
CORS(app)

epi = epitran.Epitran('fra-Latn')  # Initialisation d'Epitran pour le français

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getIPA')
def get_ipa():
    word = request.args.get('word', default='', type=str)
    if word:
        # Convertit le mot en phonèmes IPA
        ipa = epi.transliterate(word)
        return jsonify(ipa=ipa)
    else:
        return jsonify(error="No word provided"), 400

if __name__ == '__main__':
    app.run(debug=True)

