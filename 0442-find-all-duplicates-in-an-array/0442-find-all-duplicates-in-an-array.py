class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                s.append(nums[i])
        return s
        
