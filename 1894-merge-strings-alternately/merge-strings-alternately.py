class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1,n2 = len(word1),len(word2)
        x = max(n1,n2)
        s=[]
        for i in range(x):
            if i<n1:
                s.append(word1[i])
            if i<n2:
                s.append(word2[i])
        return ''.join(s) 