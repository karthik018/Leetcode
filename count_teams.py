nums = list(map(int, input().split()))

count = 0
n = len(nums)
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a, b, c = nums[i], nums[j], nums[k]
            is_team = a < b < c or a > b > c
            if is_team:
                count += 1
                
print(count)
