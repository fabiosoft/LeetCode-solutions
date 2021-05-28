class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        total = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                total = max(total, count)
        return total