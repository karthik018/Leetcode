class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev_sum = nums[0]
        res = [prev_sum]
        for num in nums[1:]:
            prev_sum += num
            res.append(prev_sum)
            
        return res
