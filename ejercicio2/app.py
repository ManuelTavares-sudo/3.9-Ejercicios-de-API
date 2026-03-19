from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    # Validar que se recibieron los datos necesarios
    if not datos or 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Se requiere 'valor' y 'escala' (C o F)"}), 400

    valor = datos['valor']
    escala = datos['escala'].upper()

    # Aplicar la fórmula de conversión según la escala de origen
    if escala == 'C':
        # Celsius a Fahrenheit: F = (C × 9/5) + 32
        resultado = (valor * 9 / 5) + 32
        escala_destino = 'F'
        nombre_origen = 'Celsius'
        nombre_destino = 'Fahrenheit'

    elif escala == 'F':
        # Fahrenheit a Celsius: C = (F - 32) × 5/9
        resultado = (valor - 32) * 5 / 9
        escala_destino = 'C'
        nombre_origen = 'Fahrenheit'
        nombre_destino = 'Celsius'

    else:
        return jsonify({"error": "La escala debe ser 'C' (Celsius) o 'F' (Fahrenheit)"}), 400

    respuesta = {
        "valor_original": valor,
        "escala_origen": nombre_origen,
        "resultado": round(resultado, 2),
        "escala_destino": nombre_destino
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True, port=5001)