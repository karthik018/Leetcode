n = int(input())
m = int(input())

A, B = [], []
for _ in range(n):
    l = list(map(int, input().split()))
    A.append(l)
for _ in range(m):
    l = list(map(int, input().split()))
    B.append(l)

i, j = 0, 0
res = []
while i < len(A) and j < len(B):
    l = max(A[i][0], B[j][0])
    r = min(A[i][1], B[j][1])
    
    if l <= r:
        res.append([l, r])
        
    if A[i][1] < B[j][1]:
        i += 1
    else:
        j += 1
    
print(res)
