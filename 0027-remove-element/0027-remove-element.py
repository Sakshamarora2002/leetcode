class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        N = len(nums)
        i = 0

        while i < N:
            if nums[i] == val:
                for j in range(i, N - 1):
                    nums[j] = nums[j + 1]
                N -= 1
            else:
                i += 1
        return N
