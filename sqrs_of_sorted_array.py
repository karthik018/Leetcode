A = list(map(int, input().split()))

neg, pos = [], []
for num in A:
	if num < 0:
		neg.append(num**2)
		continue
	pos.append(num**2)
	
neg = neg[::-1]
res = []
i, j = 0, 0
while i < len(pos) and j < len(neg):
	if pos[i] <= neg[j]:
		res.append(pos[i])
		i += 1
	else:
		res.append(neg[j])
		j += 1
		
if i < len(pos):
 	res += pos[i:]
if j < len(neg):
	res += neg[j:]
	
print(res)
