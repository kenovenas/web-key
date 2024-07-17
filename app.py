from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Armazenar as chaves geradas
generated_keys = {}

@app.route('/generate-key', methods=['GET'])
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    generated_keys[key] = True  # Armazena a chave como válida
    return jsonify(key=key)

@app.route('/validate-key', methods=['POST'])
def validate_key():
    data = request.get_json()
    key = data.get('key')
    if key in generated_keys:
        return jsonify(valid=True)
    else:
        return jsonify(valid=False)

if __name__ == "__main__":
    app.run(debug=True)
