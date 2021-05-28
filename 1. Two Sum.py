class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in table:
                table[num] = i
            else:
                return [ table[n], i ]