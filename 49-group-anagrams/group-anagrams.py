from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26 #a-z
            for c in s:
                count[ord(c)-ord('a')] += 1

            key =tuple(count) #need to make it hashable so we convert it into tuple
            anagrams[key].append(s)

        return list(anagrams.values())
#time: O(m.n)