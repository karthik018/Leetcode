m, n = map(int, input().split())
matrix = []
for _ in range(m):
	row = list(map(int, input().split()))
	matrix.append(row)
	
count = 0
for row in matrix:
	if row[0] < 0:
		count += len(row)
	elif row[-1] >= 0:
		continue
	else:
		for i in range(len(row)-1, -1, -1):
			if row[i] < 0:
				count += 1
			else:
				break

print(count)
