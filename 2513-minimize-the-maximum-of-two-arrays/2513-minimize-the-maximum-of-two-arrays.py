import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        def remaining_elements(m, divisor):
            return m - m // divisor

        d1, d2, u1, u2 = divisor1, divisor2, uniqueCnt1, uniqueCnt2
        l, r, res = 1, 10 ** 10, float('inf')

        while l <= r:
            m = (l + r) // 2
            x, y, z = remaining_elements(m, d1), remaining_elements(m, d2), remaining_elements(m, lcm(d1, d2))

            if x < u1 or y < u2 or z < u1 + u2:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
                
        return res
