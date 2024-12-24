from flask import Flask, render_template, request

app = Flask(__name__)

# Função Python que queremos usar
def calcular_soma(a, b):
    return a + b

# Rota principal para a página HTML
@app.route('/')
def home():
    return render_template('index.html')

# Rota para chamar a função Python
@app.route('/calcular', methods=['POST'])
def calcular():
    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    resultado = calcular_soma(numero1, numero2)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
