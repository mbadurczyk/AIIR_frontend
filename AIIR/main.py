from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    szyfr = request.form['szyfr']
    return render_template('deszyfrowanie.html', szyfr=szyfr)


if __name__ == '__main__':
    app.run()