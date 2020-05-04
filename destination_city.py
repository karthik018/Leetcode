n = int(input())
paths = []
for _ in range(n):
	paths.append(list(input().split()))
	
s_d = {}
for path in paths:
	s_d[path[0]] = path[1]
	
res = ""
for path in paths:
	if not s_d.get(path[1]):
		res = path[1]

print(res)
