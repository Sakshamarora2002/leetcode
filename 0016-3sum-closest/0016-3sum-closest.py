class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        D=float('inf')
        for i in range(len(nums)-1):
            A=i+1
            B=len(nums)-1
            while(A<B):
                shot=nums[i]+nums[A]+nums[B]
                if shot==target:
                    return target
                elif abs(target-shot)<D:
                    D=abs(target-shot)
                    sol=shot
                if shot>target:
                    B=B-1
                else:
                    A=A+1
        return sol


                



        