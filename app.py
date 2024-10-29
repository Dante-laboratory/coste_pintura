from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Obtener datos del formulario
        area = float(request.form['area'])
        capas = int(request.form['capas'])
        rendimiento = float(request.form['rendimiento'])
        precio = float(request.form['precio'])
        
        # Calcular costo
        cantidad_total_pintura = (area * capas) / rendimiento
        costo_total = cantidad_total_pintura * precio
        
        return jsonify({'costo_total': f"{costo_total:.2f}"})
    except ValueError:
        return jsonify({'error': 'Por favor ingresa valores numéricos válidos.'})

if __name__ == '__main__':
    app.run(debug=True)
