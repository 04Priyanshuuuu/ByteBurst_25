from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run_ava')
def run_ava():
    subprocess.Popen(["run_ava.bat"], shell=True)
    return "Ava Assistant Started"

if __name__ == '__main__':
    app.run(port=5005)
