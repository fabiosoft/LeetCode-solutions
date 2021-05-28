class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        lsum = 0
        for i, x in enumerate(nums):
            rsum = total_sum - lsum - x
            if lsum == rsum:
                return i
            lsum += x
        return -1
        