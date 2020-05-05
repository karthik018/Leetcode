s = input()
t = input()
n = len(s)

from collections import Counter
s_c, t_c = Counter(s), Counter(t)

count = 0
for c in t:
    if c not in s_c:
        count += 1
    else:
        if s_c[c]:
            s_c[c] -= 1
        else:
            count += 1
        
print(count)

