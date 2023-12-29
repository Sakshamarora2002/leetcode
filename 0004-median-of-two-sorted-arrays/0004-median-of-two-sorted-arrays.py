import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c=[]
        c=np.concatenate((nums1,nums2))
        c.sort()
        answer=np.median(c)
        return answer