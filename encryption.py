from power import *
import sys

class RSA():
    def __init__(self, p, q, e, debug=False):
        self.p, self.q, self.e, self.debug = p, q, e, debug
        self.euler = (self.p-1) * (self.q-1)
        self.n = self.p * self.q
        self.d = power(e, -1, self.euler)[0]
        print(self.d)

    def encrypt(self, x):
        return power(x, self.e, self.n, self.debug)[0]

    def decrypt(self, y):
        return power(y, self.d, self.n, self.debug)[0]

class ElGamal():
	
    def __init__(self, p, alpha, a, debug=False):
        self.p, self.alpha, self.a = p, alpha, a
        self.beta = power(alpha, a, p)[0]

    def encrypt(self, x, k):
        self.k = k
        self.y1 = power(self.alpha, k, self.p)[0]
        self.y2 = (x * power(self.beta, k, self.p)[0])  % self.p
        return self.y1, self.y2

    def decrypt(self, y):
        return (self.y2 * power(self.y1, self.p-1-self.a, self.p)[0]) % self.p

if __name__ == "__main__":
    if sys.argv[1] == '0':
        rsa = RSA(13, 29, 11)
        x = 1611
        y = rsa.encrypt(x)
        _x = rsa.decrypt(y)
        print("RSA Encryption . .  .")
        print("Message:\t{}\nEncrypted:\t{}\nDecrypted:\t{}".format(x, y, _x))
    else:
        elgamal = ElGamal(29, 2, 23)
        x = 18
        k = 15
        y = elgamal.encrypt(x, k)
        _x = elgamal.decrypt(y)
        print("Elgamal Encryption . .  .")
        print("Message:\t{}\nEncrypted:\t{}\nDecrypted:\t{}".format(x, y, _x))