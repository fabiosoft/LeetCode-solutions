class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < (n - 1):
            num = arr[i]
            if num == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 1
            i += 1
        