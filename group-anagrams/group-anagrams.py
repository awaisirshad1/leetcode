from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            sw = ''.join(sorted(s))
            if sw not in hm:
                hm[sw] = []
            hm[sw].append(s)
        result = []
        for k in hm.values():
            result.append(k)
        return result

        