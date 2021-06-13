from flask import Flask, render_template, request
from ciphey import decrypt
from ciphey.iface import Config
import os
import subprocess
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    szyfr = request.form['szyfr']

    os.system('cd ..')
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    print(THIS_FOLDER)
    my_file = os.path.join(THIS_FOLDER, 'decrypt.sh')
    os.system('ls -a')
    os.system('echo '+szyfr+' > encrypted.txt')
    output = subprocess.check_output("chmod +x decrypt.sh|sh decrypt.sh", shell=True)
    output=output.decode("utf-8")
    print("OUTPUT="+output)

    #wynik=decrypt(Config().library_default().complete_config(), szyfr)
    return render_template('deszyfrowanie.html', szyfr=output)


if __name__ == '__main__':
    app.run()