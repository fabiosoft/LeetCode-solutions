class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        i = 1
        salendo = True
        while i < n and salendo == True:
            if arr[i] == arr[i - 1]:
                return False
            if arr[i] < arr[i - 1]:
                salendo = False
            i += 1

        cima = i - 2   

        j = i
        scendendo = True
        while j < n and scendendo:
            if arr[j] >= arr[j - 1]:
                scendendo = False
            j += 1

        return cima != 0 and (not salendo and scendendo)

   