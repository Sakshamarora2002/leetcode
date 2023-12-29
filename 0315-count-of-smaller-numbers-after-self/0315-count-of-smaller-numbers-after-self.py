from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        index_map = list(range(len(nums)))  # Create a mapping of indices
        
        def merge_sort(start, end):
            if start < end:
                mid = (start + end) // 2
                merge_sort(start, mid)
                merge_sort(mid + 1, end)
                merge(start, mid, end)
        
        def merge(start, mid, end):
            i, j = start, mid + 1
            merged = []
            right_count = 0
            
            while i <= mid and j <= end:
                if nums[index_map[i]] > nums[index_map[j]]:
                    right_count += 1
                    merged.append(index_map[j])
                    j += 1
                else:
                    counts[index_map[i]] += right_count
                    merged.append(index_map[i])
                    i += 1
            
            while i <= mid:
                counts[index_map[i]] += right_count
                merged.append(index_map[i])
                i += 1
            
            while j <= end:
                merged.append(index_map[j])
                j += 1
            
            for k in range(len(merged)):
                index_map[start + k] = merged[k]
        
        merge_sort(0, len(nums) - 1)
        return counts


