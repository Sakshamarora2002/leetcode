class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        x1=bin(x)[2:]
        y1=bin(y)[2:]
        maxl=max(len(x1),len(y1))
        x1=x1.zfill(maxl)
        y1=y1.zfill(maxl)
        for i in range(maxl):
            if x1[i]!=y1[i]:
                c+=1
        return c
