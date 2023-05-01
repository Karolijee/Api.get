from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo': 'Twilight',
        'autor': 'Stephenie Meyer'
    },
    {
        'id':2,
        'titulo': 'Se nao eu, quem vai fazer voce feliz?',
        'autor': 'Graziela Goncalves'
    },
    {
        'id':3,
        'titulo': 'O alquimista',
        'autor': 'Paulo Coelho'
    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify (livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livro:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify[livros]





app.run(port=5000,host='localhost', debug=True)
