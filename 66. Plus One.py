class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsLen = len(digits)
        for i in reversed(range(digitsLen)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else: #49
                digits[i] = 0
        #100
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits