s = open('24.txt').readline()
k = 0
mn = 999999
for i in range(len(s)):
    if s[i] != ' ':
        k += 1
        if k < mn:
            mn = k
    else:
        k = 0
print(mn)
