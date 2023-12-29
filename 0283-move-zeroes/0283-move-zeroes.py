class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = len(nums)
        count_zeros = nums.count(0) 
        non_zero_index = 0

        for i in range(l):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        for i in range(non_zero_index, l):
            nums[i] = 0

        return nums
