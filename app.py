from flask import Flask, jsonify, request
import psycopg2 as psycopg2

app = Flask(__name__)

dataset = [
    {
        'id': 1,
        'nome_coluna': 'satélite01',
        'lat': '1111111',
        'long': '1111111'
    },
    {
        'id': 2,
        'nome_coluna': 'satélite02',
        'lat': '1111111',
        'long': '1111111'
    },
    {
        'id': 3,
        'nome_coluna': 'satélite03',
        'lat': '1111111',
        'long': '1111111'
    },
    {
        'id': 4,
        'nome_coluna': 'satélite04',
        'lat': '1111111',
        'long': '1111111'
    }
]


# TODO: EXIBINDO TODOS OS DADOS CADASTRADOS
@app.route('/cords', methods=['GET'])
def home():
    return jsonify(dataset), 200


# TODO: Inserindo informações contidas no JSON no banco
@app.route('/cords/bd', methods=['GET'])
def insert_into_bd():
    # todo: conectando com o banco
    con = psycopg2.connect(host='localhost', database='postgres',
                           user='postgres', password='postgres')
    cur = con.cursor()

    x = 0
    while (x < len(dataset)):
        # todo: inserindo no banco
        sql = "insert into cord values (" + str(dataset[x]['id']) + ",'" + str(dataset[x]['nome_coluna']) + "'," + \
              str(dataset[x]['lat']) + "," + str(dataset[x]['long']) + ")"
        cur.execute(sql)
        con.commit()
        x += 1
    return jsonify({'message': 'Coordenadas adicionadas no banco'}), 200


# TODO: BUSCANDO INFORMAÇÃO DO JSON POR ID
@app.route('/cords/<int:id>', methods=['GET'])
def cord_per_id(id):
    for data in dataset:
        if data['id'] == id:
            return jsonify(data), 200

    return jsonify({'error': 'Coordenada não encontrada'}), 404


# TODO: INSERINDO JSON VIA POST
@app.route('/cords', methods=['POST'])
def save_cord():
    data = request.get_json()
    dataset.append(data)
    return jsonify(data), 201


# TODO: DELETANDO PARTE DO JSON VIA ID (ESTÁ DELETANDO POR POSIÇÃO DO ARRAY)
@app.route('/cords/<int:id>', methods=['DELETE'])
def remove_cord(id):
    index = id - 1
    del dataset[index]

    return jsonify({'message': 'Coordenada deletada'}), 200

if __name__ == '__main__':
    app.run(debug=True)

