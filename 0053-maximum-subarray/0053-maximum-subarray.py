class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, start, end):
            if start == end:
                return nums[start]

            mid = (start + end) // 2

            left_sum = divide_and_conquer(nums, start, mid)

            right_sum = divide_and_conquer(nums, mid + 1, end)

            cross_sum = 0
            left_cross_sum = float('-inf')
            for i in range(mid, start - 1, -1):
                cross_sum += nums[i]
                left_cross_sum = max(left_cross_sum, cross_sum)

            cross_sum = 0
            right_cross_sum = float('-inf')
            for i in range(mid + 1, end + 1):
                cross_sum += nums[i]
                right_cross_sum = max(right_cross_sum, cross_sum)

            return max(left_sum, right_sum, left_cross_sum + right_cross_sum)

        return divide_and_conquer(nums, 0, len(nums) - 1)
