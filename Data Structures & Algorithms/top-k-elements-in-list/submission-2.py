from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_list = Counter(nums)
        descending_keys = sorted(counter_list, key=counter_list.get, reverse=True)

        return descending_keys[:k]