from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_list = Counter(nums)
        descending_keys = sorted(Counter(nums), key=Counter(nums).get, reverse=True)

        return descending_keys[:k]