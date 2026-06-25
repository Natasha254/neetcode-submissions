class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for str in strs:
            sortedstr = ''.join(sorted(str))
            group[sortedstr].append(str)

        return list(group.values())

        


