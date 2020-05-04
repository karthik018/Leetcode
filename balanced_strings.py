s = input()
stack = []
n = len(s)
stack.append(s[0])
count = 0
for i in range(1, n):
	if stack:
		if stack[-1] != s[i]:
			stack.pop()
			if not len(stack):
				count += 1
		else:
			stack.append(s[i])
	else:
		stack.append(s[i])

print(count)

