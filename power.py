from extended_euclide import *

def binary(x):
    return bin(x)[2:]

def power(a, b, m, debug=False):
    # a^b mod m
    res, table = None, None
    if b == -1:
        res, table = extended_euclide(a, m, True)
    else:
        bits = binary(b)
        x = 1
        base = a % m
        idx = 0
        table = [["" for j in range(5)] for i in range(len(bits)+1)]
        table[0] = ['i', 'bit', 'x', 'base']
        if debug:
            print("{}\t{}\t{}\t{}".format('i', 'bit', 'x', 'base'))
        for bit in bits[::-1]:
            x = x if bit == '0' else (x * base) % m
            base = (base * base) % m
            table[idx+1] = [str(idx), str(bit), str(x), str(base)]
            if debug:
                print("{}\t{}\t{}\t{}".format(idx, bit, x, base))
            idx = idx + 1
        res = x
    return res, table

if __name__ == "__main__":
	power(19, 15, 142, True)