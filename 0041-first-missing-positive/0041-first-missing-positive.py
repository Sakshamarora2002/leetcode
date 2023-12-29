class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        num = 1
        while num in nums_set:
            num += 1
        return num

