import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            str_copy = nums.copy()
            str_copy.pop(i)
            result.append(math.prod(str_copy))

        return result