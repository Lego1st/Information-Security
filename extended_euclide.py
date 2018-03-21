import argparse
import sympy



# def extended_euclide(a, b):
# 	""" calculate b^(-1) mod a == t mod a"""
# 	a0, b0 = a, b
# 	t0, t = 0, 1
# 	s0, s = 1, 0
# 	q = int(a0/b0)
# 	r = a0-q*b0
# 	while r > 0:
# 		t0, t = t, t0-q*t
# 		s0, s = s, s0-q*s
# 		a0, b0 = b0, r
# 		q = int(a0/b0)
# 		r = a0-q*b0
# 	r = b0
# 	return (r, s, t)


def extended_euclide(a, b, debug=False):
	q = [b, a]
	r = []
	s = [1, 0]
	while q[-1] != 0:
		r.append(q[-2] // q[-1])
		q.append(q[-2] % q[-1])
	r.extend(r[::-1])
	n = len(q)-2
	for i in range(0, n, 1):
		s.append((s[-2] - r[n+i] * s[-1]) % b)

	table = [["" for j in range(6)] for i in range(n+2)]
	table[0] = ['q(i-1)', 'q(i)', 'r(i)', 'q(i+1)', 's(i-1)', 's(i)']
	for i in range(n):
		table[1+i][0] = str(q[i])
	for i in range(1, n+1):
		table[1+i-1][1] = str(q[i])
	for i in range(2, n+2):
		table[1+i-2][3] = str(q[i])
	for i in range(n):
		table[1+i][2] = str(r[i])
	for i in range(n+1):
		table[1+i][4], table[1+i][5] = str(s[i]), str(s[i+1])
	if debug:
		for i in range(n+2):
			print("{}\t{}\t{}\t{}\t{}\t{}\n".format(table[i][0], table[i][1], table[i][2], table[i][3], table[i][4], table[i][5]))
	return s[-1], table
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("x", type=int)
	parser.add_argument("y", type=int)
	args = parser.parse_args()
	A, B = args.x, args.y
	tmp = extended_euclide(A, B, True)
	print("A: {}\nB: {}\n".format(A, B))
	# print("(r, s, t): {}".format(tmp))
	print("{}^(-1) mod {} = {}".format(A, B, tmp))
