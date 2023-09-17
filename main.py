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

""" def get_video_as_base64(video_filename):
    with open(f"static/videos/{video_filename}", "rb") as video_file:
        video_data = video_file.read()
        base64_video = base64.b64encode(video_data).decode('utf-8')
    return base64_video """

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
@app.route('/lecciones/<int:id_leccion>/<int:id_seccion>', methods=['GET'])
def getLecciones(id_leccion, id_seccion):
    if id_leccion == 1:
        for item in abecedario:
            if item['id'] == id_seccion:
                item['imagen64'] = get_image_as_base64(item['imagen'])
                """ item['video'] = get_video_as_base64(item['video_filename']) """
                return jsonify(item)
        return jsonify({"error": "Letra no encontrada."}), 404
    elif id_leccion == 2:
        for item in saludos:
            if item['id'] == id_seccion:
                item['imagen64'] = get_image_as_base64(item['imagen'])
                """ item['video'] = get_video_as_base64(item['video_filename']) """
                return jsonify(item)
        return jsonify({"error": "Saludo no encontrado."}), 404
    elif id_leccion == 3:
        for item in numeros:
            if item['id'] == id_seccion:
                item['imagen64'] = get_image_as_base64(item['imagen'])
                """ item['video'] = get_video_as_base64(item['video_filename']) """
                return jsonify(item)
        return jsonify({"error": "Número no encontrado."}), 404
    else:
        return jsonify({"error": "Lección no encontrada."}), 404
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)