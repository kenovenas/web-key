from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verificar-chave', methods=['POST'])
def verificar_chave():
    data = request.get_json()
    chave = data.get('chave')

    # Lógica para validar a chave (exemplo simples)
    chave_valida = False
    if chave == 'chave_correta':
        chave_valida = True

    # Retorna a resposta como JSON
    return jsonify({'valido': chave_valida})

if __name__ == '__main__':
    app.run(debug=True)
