class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count  = 0
        hash = set()
        left = 0
        right = 0
        n = len(s)
        while right < n:
            
            while s[right] in hash:
                hash.discard(s[left])
                left +=1
                
            else:
                hash.add(s[right])
                right +=1
            count = max(count,len(hash))
           
        return count
            
