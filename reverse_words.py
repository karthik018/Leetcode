s = input()
s = s.strip()

s_l = s.split()
n = len(s_l)
res = []
for i in range(n-1, -1, -1):
    res.append(s_l[i].strip())

res = ' '.join(res)
print(res)
