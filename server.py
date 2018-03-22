from flask import Flask, request, json, render_template
from power import *
from encryption import *
import digital_signature

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/power", methods=["POST"])
def power_serve():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    m = int(request.form.get('m'))
    _, result = power(a, b, m, True)
    return render_template('power.html', table = result)

@app.route("/rsa", methods=["POST"])
def rsa_serve():
    p = int(request.form.get('p'))
    q = int(request.form.get('q'))
    e = int(request.form.get('e'))
    x = int(request.form.get('x'))
    rsa = RSA(p, q, e, True)
    y = rsa.encrypt(x)
    _x = rsa.decrypt(y)
    data = rsa.__dict__
    data['y'] = y
    data['_x'] = _x
    data['x'] = x
    return render_template('encryption.html', data = data.items(), encrypt = 'RSA')

@app.route("/elgamal", methods=["POST"])
def elgamal_serve():
    p = int(request.form.get('p'))
    alpha = int(request.form.get('alpha'))
    a = int(request.form.get('a'))
    k = int(request.form.get('k'))
    x = int(request.form.get('x'))
    elgamal = ElGamal(p, alpha, a, True)
    y = elgamal.encrypt(x, k)
    _x = elgamal.decrypt(y)
    data = elgamal.__dict__
    data['y'] = y
    data['_x'] = _x
    data['x'] = x
    return render_template('encryption.html', data = data.items(), encrypt = 'Elgamal')

@app.route("/rsa_sign", methods=["POST"])
def rsa_sign_serve():
    pa = int(request.form.get('pa'))
    qa = int(request.form.get('qa'))
    ea = int(request.form.get('ea'))
    pb = int(request.form.get('pb'))
    qb = int(request.form.get('qb'))
    eb = int(request.form.get('eb'))
    x = int(request.form.get('x'))
    rsa = digital_signature.RSA(pa, qa, ea, pb, qb, eb, x)
    y = rsa.mess_encrypt()
    _x = rsa.mess_decryt()
    rsa.sign()
    rsa.ver()
    data = rsa.__dict__
    # data['y'] = y
    # data['_x'] = _x
    # data['x'] = x
    return render_template('digital_sign.html', data = data.items(), encrypt = 'RSA')

@app.route("/elgamal_sign", methods=["POST"])
def elgamal_sign_serve():
    p = int(request.form.get('p'))
    alpha = int(request.form.get('alpha'))
    a = int(request.form.get('a'))
    k = int(request.form.get('k'))
    x = int(request.form.get('x'))
    elgamal = digital_signature.ElGamal(p, alpha, a, k, x, True)
    elgamal.sign()
    elgamal.ver()
    data = elgamal.__dict__
    # data['y'] = y
    # data['_x'] = _x
    # data['x'] = x
    return render_template('digital_sign.html', data = data.items(), encrypt = 'Elgamal')

if __name__ == "__main__":
    app.run(port=5111)