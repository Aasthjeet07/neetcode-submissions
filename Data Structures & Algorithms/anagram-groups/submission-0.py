class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i in strs:
            sorted_w = "".join(sorted(i))
            m[sorted_w].append(i)
        
        return list(m.values())


            
