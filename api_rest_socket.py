# server.py
# giovanni barrero ortiz
from flask import Flask, request, jsonify

app = Flask("prueba")

@app.route('/rpc', methods=['POST'])
def rpc_server():
    data = request.get_json()
    if data is not None and 'method' in data and 'params' in data:
        method = data['method']
        params = data['params']

        # Implementa la lógica del servidor RPC aquí
        if method == 'sumar':
            result = sum(params)
        elif method == 'restar':
            result = params[0] - params[1]
        else:
            return jsonify({"error": "Método no encontrado"}), 404

        return jsonify({"result": result})
    else:
        return jsonify({"error": "Solicitud incorrecta"}), 400

if __name__ == '__main__':
    app.run(debug=True)