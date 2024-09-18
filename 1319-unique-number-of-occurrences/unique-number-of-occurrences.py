from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        occur=list(count.values())
        return len(occur)==len(set(occur))
        