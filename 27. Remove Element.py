class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums)
        while i > 0:
            i -= 1
            num = nums[i]
            if num == val:
                nums.pop(i)