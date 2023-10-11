x = 4 ** 2100 - 64 ** 30 - 8
k = 0
while x > 0:
    if x % 4 == 3:
        print(x)
        k += 1
    x // 4
print(k)
