class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set()
        result = []
        
        for perm in permutations(nums):
            if perm not in perms:
                perms.add(perm)
                result.append(list(perm))
        
        return result
