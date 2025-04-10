from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Funzione per leggere i dati dal CSV
def leggi_dati():
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        return list(reader)

# Funzione per scrivere i dati nel CSV
def scrivi_dati(dati):
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dati)

# Route per visualizzare i dati
@app.route('/')
def visualizza_dati():
    dati = leggi_dati()
    return render_template('index.html', dati=dati)

# Route per inserire o modificare i dati
@app.route('/index', methods=['GET', 'POST'])
def modifica_dati():
    if request.method == 'POST':
        nome = request.form['nome']
        eta = request.form['eta']
        dati = leggi_dati()
        dati.append([nome, eta])
        scrivi_dati(dati)
        return redirect(url_for('visualizza_dati'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
