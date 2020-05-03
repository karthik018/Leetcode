nums = list(map(int, input().split()))
temp = sorted(nums)

n = len(nums)

less_count = {}
res = []
for i in range(n):
    if less_count.get(temp[i]) is None:
        less_count[temp[i]] = i
 
for num in nums:
    res.append(less_count[num])
    
print(res)
        
