from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                duplicate_nums = nums[j + 1:]  # Create a duplicate array from j+1 to the end
                
                left = 0
                right = len(duplicate_nums) - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + duplicate_nums[left] + duplicate_nums[right]
                    
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], duplicate_nums[left], duplicate_nums[right]])
                        
                        while left < right and duplicate_nums[left] == duplicate_nums[left + 1]:
                            left += 1
                        while left < right and duplicate_nums[right] == duplicate_nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

