class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            num = nums[i]
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums