words = list(input().split())
pattern = input()

res = []
n = len(pattern)

for word in words:
    flag = True
    rel = {}
    mapped = []
    for i in range(n):
        if pattern[i] in rel:
            if rel[pattern[i]] != word[i]:
                flag = False
                break
        else:
            if word[i] not in mapped:
                rel[pattern[i]] = word[i]
                mapped.append(word[i])
            else:
                flag = False
                break
    if flag:
        res.append(word)
        
print(res)
