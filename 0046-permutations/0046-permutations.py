class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=permutations(nums)
        R=[list(p)for p in perms]
        return R