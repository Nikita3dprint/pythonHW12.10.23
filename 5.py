for n in range(1, 200):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += '00'
    else:
        b += '10'
    r = int(b, 2)
    if r > 130:
        print(n)
        break
        