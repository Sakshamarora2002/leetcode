class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        remgas=0
        ans=1000000002
        for i in range(0,len(gas)):
            remgas+=gas[i]-cost[i]
            if remgas<0:
                remgas=0
                ans=1000000002
            else:
                ans=min(i,ans)
        return ans