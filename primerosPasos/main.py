from flask import Flask, jsonify, request
app = Flask(__name__)

users = [
    {'id': "25",'name': 'pepe','telefono': "1234567890"},
    {'id': "15",'name': 'luis','telefono': "1234567890"},
    {'id': "5",'name': 'roberto','telefono': "1234567890"},
]

# ruta principal
@app.route('/')
def root():
    return 'Hola programadores de python'

# obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users), 201 

# obtener usuario por id
@app.route('/users/<user_id>')  
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), "No existe ese usuario")
    return jsonify(user), 200

# crear usuario
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    data['status'] = 'CREATED'
    return jsonify(data), 201 


# modificar usuario
@app.route('/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user), 200
    else:
        return "No existe ese usuario", 404


if __name__ == '__main__':
    app.run(debug=True)

