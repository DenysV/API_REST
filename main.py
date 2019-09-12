# -*- coding: utf-8 -*-

# Se debe implementar un Web Service utilizando cualquier framework que incluya
# los siguientes servicios (Flask está en las dependencias del proyecto pero se puede
# utilizar Django o cualquier otro Framework. Solo asegurate de modificar las dependencias en el fichero
# requirements.txt):
import json

from flask import Flask, request
from flask_restplus import Resource, fields, Api, Namespace
from utils.matrix import elements_sum, diagonal_sum
from utils.compression import encode

app = Flask(__name__)
api = Api(app, version='1.0', title='Test exercises', description='An API of test exercises')
ns = api.namespace('TEST', description='Intelygenz talent test')

matrix = api.model("matrix", {"matrix": fields.String("Elements of matrix.")})
string = api.model("string", {"string": fields.String("Word")})

# POST: /api/matrix/sum
# =====================
# Debe devolver la suma de todos los elementos de una matriz
# dada. Se debe implementar usando la función utils.matrix.elements_sum
# Ejemplo de llamada:
# --------------------------------------------------
# Content-Type: application/json
#
# { "matrix": [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] }
# --------------------------------------------------
# Ejemplo de respuesta:
# --------------------------------------------------
# Content-Type: application/json
#
# { "result": 45 }
# --------------------------------------------------

@ns.route('/api/matrix/sum')
class Sum(Resource):
    @api.doc('Sum of matrix elements')
    @api.expect(matrix)
    def post(self):
        """Sum of matrix elements"""
        if request.is_json:
            data = request.get_json().get('matrix')
            res = elements_sum(data)
            stat = 200 if isinstance(res, int) else 400
            response = app.response_class(response=json.dumps({'result':res}),status=stat, mimetype='application/json')
        else:
            response = app.response_class(response='Input data is not in JSON format', status=400, mimetype='application/json')
        return response
# POST: /api/matrix/diagonal_sum
# ==============================
# Debe devolver la suma de los elementos de la diagonal principal de una matriz
# dada. Se debe implementar usando la función utils.matrix.diagonal_sum
# Ejemplo de llamada:
# --------------------------------------------------
# Content-Type: application/json
#
# { "matrix": [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] }
# --------------------------------------------------
# Ejemplo de respuesta:
# --------------------------------------------------
# Content-Type: application/json
#
# { "result": 15 }
# --------------------------------------------------

@ns.route('/api/matrix/diagonal_sum')
class Diagonal_sum(Resource):
    @api.expect(matrix)
    def post(self):
        """Diagonal principal of matrix"""
        if request.is_json:
            data = request.get_json().get('matrix')
            res = diagonal_sum(data)
            stat = 200 if isinstance(res, int) else 400
            response = app.response_class(response=json.dumps({'result':res}),status=stat, mimetype='application/json')
        else:
            response = app.response_class(response='Input data is not in JSON format', status=400, mimetype='application/json')
        return response

# POST: /api/string/encode
# ========================
# Debe devolver el string dado codificado de la siguiente manera:
# Por cada grupo de caracteres alfabéticos (de la A a la Z sin incluir la Ñ y sin distinguir mayúsculas
# de minúsculas) iguales consecutivos, se incluira dicho caracter en mayúsculas seguido del número de repeticiones.
# Se debe implementar utilizando la función utils.compression.encode
# Ejemplo de llamada:
# --------------------------------------------------
# Content-Type: application/json
#
# { "string": "aaAabaccCBb" }
# --------------------------------------------------
# Ejemplo de respuesta:
# --------------------------------------------------
# Content-Type: application/json
#
# { "result": "A4B1A1C3B2" }
@ns.route('/api/string/encode')
class Encode_string(Resource):
    @api.expect(string)
    def post(self):
        """Encode string"""
        if request.is_json:
            data = request.get_json().get('string')
            res = encode(data)
            stat = 400 if res == 'Word %s has spanish letters.' % data else 200
            response = app.response_class(response=json.dumps({'result':res}), status=stat, mimetype='application/json')
        else:
            response = app.response_class(response='Input data is not in JSON format', status=400, mimetype='application/json')
        return response

app.run(host='0.0.0.0', port=5000)
