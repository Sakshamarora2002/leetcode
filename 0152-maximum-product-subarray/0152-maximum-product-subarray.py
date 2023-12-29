class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax,cmin=1,1
        res=nums[0]
        for n in nums:
            values=(n,cmax*n,cmin*n)
            cmax,cmin=max(values),min(values)
            res=max(res,cmax)
        return res