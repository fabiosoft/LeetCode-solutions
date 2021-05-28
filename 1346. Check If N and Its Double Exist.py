class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        j = 0
        for i in range(n):
            j = 0
            while j < n:
                if i != j and (arr[i] == arr[j] * 2):
                    return True
                j += 1
        return False