class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        two_Sum = defaultdict(int)
        for i in range(len(numbers)):
            second_element = target - numbers[i]
            if two_Sum[second_element]:
                return [two_Sum[second_element], i+1]
            two_Sum[numbers[i]] = i + 1

        return []

        
