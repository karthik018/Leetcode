nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums = list(set(nums1+nums2))

from collections import Counter
nums1_counter = Counter(nums1)
nums2_counter = Counter(nums2)

res = []
for num in nums:
	if num in nums1_counter and num in nums2_counter:
		if nums1_counter[num] >= 1 and nums2_counter[num] >= 1:
			res.append(num)
			
print(res)
