# app.py

from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/generate-key', methods=['GET'])
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return jsonify({'key': key})

@app.route('/validate-key', methods=['POST'])
def validate_key():
    data = request.get_json()
    key_to_validate = data.get('key')

    # Exemplo de validação simples
    valid_keys = ['abc123', 'def456']  # Lista de chaves válidas
    if key_to_validate in valid_keys:
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

if __name__ == '__main__':
    app.run(debug=True)
