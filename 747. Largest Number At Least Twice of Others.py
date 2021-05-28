class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = -1 #4
        maxIndex = -1 #3
        for i, num in enumerate(nums):
            if num > m:
                m = num
                maxIndex = i
        for i, num in enumerate(nums):
            if maxIndex != i and nums[maxIndex] < 2 * nums[i]:
                return -1
        return maxIndex