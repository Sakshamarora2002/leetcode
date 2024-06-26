class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = len(digits)

        for i in range(k - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits
