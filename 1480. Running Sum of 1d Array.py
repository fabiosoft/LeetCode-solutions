class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        sums = []
        for i, num in enumerate(nums):
            summ += num
            sums.insert(i, summ)
        return sums
            