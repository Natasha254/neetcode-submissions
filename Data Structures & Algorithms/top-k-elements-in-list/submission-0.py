from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter_list = Counter(nums)
        descending_keys = sorted(counter_list, key=counter_list.get, reverse=True)
        for i in range(k):
            result.append(descending_keys[i])

        return result