l = list(map(int, input().split()))
e = int(input())

maxm = max(l)
res = []
for x in l:
    tot = x + e
    if tot >= maxm:
        res.append(True)
    else:
        res.append(False)
        
print(res)
