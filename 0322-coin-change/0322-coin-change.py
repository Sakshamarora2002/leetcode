class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def fn(i, amount):
            if amount == 0:
                return 0
            if amount < 0 or i < 0:
                return float('inf')
            
            using_current = 1 + fn(i, amount - coins[i]) if amount >= coins[i] else float('inf')
            not_using_current = fn(i - 1, amount)
            
            return min(using_current, not_using_current)
        
        result = fn(len(coins) - 1, amount)
        return -1 if result == float('inf') else result
