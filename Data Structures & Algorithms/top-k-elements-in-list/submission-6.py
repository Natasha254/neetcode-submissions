from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        counter_list = Counter(nums)

        for key, value in counter_list.items():
            freq[value].append(key)

        result = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result

        return result