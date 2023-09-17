from flask import Flask, jsonify
import base64
from flask_cors import CORS

from lecciones import lecciones
from lecciones import abecedario
from lecciones import numeros
from lecciones import saludos

app = Flask(__name__)

def get_image_as_base64(image_filename):
    with open(f"static/images/{image_filename}", "rb") as image_file:
        image_data = image_file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
    return base64_image

@app.route('/aprende', methods=['GET'])
def aprende():
    return jsonify(lecciones)

# 1ra Opción

@app.route('/abecedario/<int:id>', methods=['GET'])
def getAbecedario(id):
    for item in abecedario:
        if item['id'] == id:
            return jsonify(item)
    return jsonify({"error": "Letra no encontrada."}), 404

@app.route('/numero/<int:id>', methods=['GET'])
def getNumeros(id):
    for item in numeros:
        if item['id'] == (id):
            return jsonify(item)
    return jsonify({"error": "Número no encontrado."}), 404

@app.route('/saludo/<int:id>', methods=['GET'])
def getSaludos(id):
    for item in saludos:
        if item['id'] == (id):
            return jsonify(item)
    return jsonify({"error": "Saludo no encontrado."}), 404

# 2da Opción
@app.route('/lecciones/<string:leccion>/<int:id>', methods=['GET'])
def getLecciones(leccion, id):
    if leccion == 'abecedario':
        for item in abecedario:
            if item['id'] == id:
                item['imagen'] = get_image_as_base64(item['imagen'])
                return jsonify(item)
        return jsonify({"error": "Letra no encontrada."}), 404
    elif leccion == 'numeros':
        for item in numeros:
            if item['id'] == id:
                item['imagen'] = get_image_as_base64(item['imagen'])
                return jsonify(item)
        return jsonify({"error": "Número no encontrado."}), 404
    elif leccion == 'saludos':
        for item in saludos:
            if item['id'] == id:
                item['imagen'] = get_image_as_base64(item['imagen'])
                return jsonify(item)
        return jsonify({"error": "Saludo no encontrado."}), 404
    else:
        return jsonify({"error": "Lección no encontrada."}), 404
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)