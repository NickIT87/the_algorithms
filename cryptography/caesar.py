alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip()
res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')

dcp = ''
for i in res:
    dcp += alpha[(alpha.index(i) + len(alpha) - (n % len(alpha))) % len(alpha)]

print(dcp)