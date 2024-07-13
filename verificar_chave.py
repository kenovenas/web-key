from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar chaves válidas geradas pelo site
chaves_validas = []

# Endpoint para receber a chave e verificar
@app.route('/verificar-chave', methods=['POST'])
def verificar_chave():
    dados = request.get_json()
    chave_recebida = dados.get('chave')

    # Verifica se a chave recebida está na lista de chaves válidas
    if chave_recebida in chaves_validas:
        # Se encontrada, remove a chave da lista para evitar reutilização
        chaves_validas.remove(chave_recebida)
        return jsonify({'valido': True}), 200
    else:
        return jsonify({'valido': False}), 403

# Rota para adicionar uma nova chave válida (para simulação)
@app.route('/adicionar-chave', methods=['POST'])
def adicionar_chave():
    dados = request.get_json()
    nova_chave = dados.get('nova_chave')
    chaves_validas.append(nova_chave)
    return jsonify({'mensagem': 'Chave adicionada com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)
