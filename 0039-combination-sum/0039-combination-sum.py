from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.combinationSumRecursive(candidates, target, [], result)
        return result

    def combinationSumRecursive(self, candidates: List[int], target: int, current_combination: List[int], result: List[List[int]]) -> None:
        if target == 0:
            result.append(current_combination)
            return

        if target < 0:
            return

        for i in range(len(candidates)):
            self.combinationSumRecursive(candidates[i:], target - candidates[i], current_combination + [candidates[i]], result)
