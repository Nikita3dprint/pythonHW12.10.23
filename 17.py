def isfour(b):
    while b > 0:
        if b % 10 == 4:
            return 1
        b = b // 10
    return 0


a = [int(x) for x in open('17.txt')]
k = 0
mx = -10001
for i in range(len(a)):
    if isfour(a[i]) == 1:
        k += 1
        if a[i] > mx:
            mx = a[i]
print(k, mx)
