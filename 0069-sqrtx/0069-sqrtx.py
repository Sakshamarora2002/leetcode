class Solution:
    def mySqrt(self, x: int) -> int:
        #Binary search technique
        if x==0:
            return 0
        left,right=1,x
        while left<=right:
            mid=left+(right-left)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            elif mid*mid>x:
                right=mid-1
        return right
                
        