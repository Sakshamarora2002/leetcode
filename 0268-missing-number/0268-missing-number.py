class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  
        a = len(nums)
        
        if a > 1:
            # Check for the missing number between the two elements
            if nums[0] != 0:
                return 0
            for i in range(a - 1):
                if nums[i] + 1 != nums[i + 1]:
                    return nums[i] + 1
            
            # If the loop completes, the missing number is at the end of the sorted list
            return nums[-1] + 1
        else:
            # Handle the case when there are only one or no elements in the list
            return 0 if nums[0] == 1 else 1
