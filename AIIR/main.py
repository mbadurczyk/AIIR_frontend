from flask import Flask, render_template, request
from ciphey import decrypt
from ciphey.iface import Config
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    szyfr = request.form['szyfr']
    wynik=decrypt(Config().library_default().complete_config(), szyfr)
    return render_template('deszyfrowanie.html', szyfr=wynik)


if __name__ == '__main__':
    app.run()