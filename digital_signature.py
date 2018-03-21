from power import *

class RSA():
	def __init__(self, pa, qa, ea, pb, qb, eb, x):
		self.pa, self.qa, self.ea, self.pb, self.qb, self.eb, self.x = pa, qa, ea, pb, qb, eb, x
		self.na, self.nb = self.pa * self.qa, self.pb * self.qb
		self.euler_a, self.euler_b = (self.pa-1) * (self.qa-1), (self.pb-1) * (self.qb-1)
		self.da = power(self.ea, -1, self.euler_a)[0]
		self.db = power(self.eb, -1, self.euler_b)[0]
		
	def mess_encrypt(self):
		self.y = power(self.x, self.eb, self.nb)[0]
		return self.y

	def sign(self):
		self.y_sign = power(self.x, self.da, self.na)[0]
		return self.y_sign

	def mess_decryt(self):
		return power(self.y, self.db, self.nb)[0] 

	def ver(self):
		one = power(self.y_sign, self.ea, self.na)[0]
		two = self.x % self.na
		return one == two, one, two

class ElGamal():
	"""
		Return (gamma, delta)
	"""
	def __init__(self, p, alpha, a, k, x, debug = False):
		self.p, self.alpha, self.a, self.k, self.x, self.debug = p, alpha, a, k, x, debug

	def sign(self):
		self.beta = power(self.alpha, self.a, self.p, self.debug)[0]

		self.gamma = power(self.alpha, self.k, self.p, self.debug)[0]
		delta1, delta2 = (self.x - self.a * self.gamma) % (self.p-1), power(self.k, -1, self.p-1, self.debug)[0]
		self.delta = (delta1 * delta2) % (self.p-1)

		return self.gamma, self.delta

	def ver(self):
		one = (power(self.beta, self.gamma, self.p, self.debug)[0] * power(self.gamma, self.delta, self.p, self.debug))[0] % self.p
		two = power(self.alpha, self.x, self.p, self.debug)[0]
		return one == two, one, two

class DSS():
	"""
		Return (gamma, delta)
	"""
	def __init__(self, p, q, alpha, a, k, x, debug = False):
		self.p, self.q, self.alpha, self.a, self.k, self.x, self.debug = p, q, alpha, a, k, x, debug

	def sign(self):
		self.beta = power(self.alpha, self.a, self.p, self.debug)[0]

		self.gamma = power(self.alpha, self.k, self.p, self.debug)[0] % self.q
		delta1, delta2 = (self.x + self.a * self.gamma) % (self.q), power(self.k, -1, self.q, self.debug)[0]
		self.delta = (delta1 * delta2) % (self.q)

		return self.gamma, self.delta

	def ver(self):
		e1 = (self.x * power(self.delta, -1, self.q))[0] % self.q
		e2 = (self.gamma * power(self.delta, -1, self.q))[0] % self.q
		print("e1 = {}\ne2 = {}".format(e1, e2))
		one = ((power(self.alpha, e1, self.p)[0] * power(self.beta, e2, self.p)[0]) % self.p) % self.q
		two = self.gamma
		return one == two, one, two

if __name__ == "__main__":
	# print("ELGAMAL DOING . . .")
	# elGamal = ElGamal(587, 2, 318, 213, 182, False)
	# print("(Gamma,Delta) = {}".format(elGamal.sign()))
	# print("(Check,BetaGamma2...,AlphaX) = {}".format(elGamal.ver()))
	# print("\n")

	# print("RSA DOING . . .")
	# rsa = RSA(29, 37, 127, 43, 61, 101, 15)
	# rsa.mess_encrypt()
	# print("RSA key = {}".format(rsa.sign()))
	# print("Verifying... = {}".format(rsa.ver()))
	# print("Decrypted message = {}".format(rsa.mess_decryt()))

	print("DSS DOING . . .")
	dss = DSS(7879, 101, 170, 75, 50, 355)
	print("DSS key = {}".format(dss.sign()))
	print("Verifying... = {}".format(dss.ver()))