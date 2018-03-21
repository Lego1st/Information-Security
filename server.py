from flask import Flask, request, json, render_template
from power import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/eeuclid", methods=["POST"])
def eeuclid():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    m = int(request.form.get('m'))
    _, result = power(a, b, m, True)
    return render_template('eeuclid.html', table = result)

if __name__ == "__main__":
    app.run(host='192.168.1.38', port=5111)