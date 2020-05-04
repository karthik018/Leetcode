s = input()
res = ""
n = len(s)
for i in range(n-1):
	if s[i+1] == '.':
		res += s[i] + '['
	elif s[i] == '.':
		res += s[i] + ']'
	else:
		res += s[i]

res += s[n-1]
		
print(res)
