n = int(input())
k = int(input())
mat = []
for _ in range(n):
    l = list(map(int, input().split()))
    mat.append(l)
    
c = len(mat[0])
s_c = {}
for i, row in enumerate(mat):
    mid = c // 2
    if row[-1] == 1:
        s_c[i] = c
    elif row[mid] == 0:
        j = mid - 1
        while j >= 0:
            if row[j] == 1:
                break
            j -= 1
        s_c[i] = j + 1
    elif row[mid] == 1:
        j = mid + 1
        while j < c:
            if row[j] == 0:
                break
            j += 1
        s_c[i] = j
        
s_c = {k: v for k, v in sorted(s_c.items(), key=lambda item: (item[1], item[0]))}
res = list(s_c.keys())[:k]
    
print(res)
