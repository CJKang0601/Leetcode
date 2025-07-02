class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # ans = []
        n1 = len(word1)
        n2 = len(word2)
        n = min(n1,n2)
        ans = []
        for i in range(n):
            # ans += word1[i] + word2[i]
            ans.append(word1[i])
            ans.append(word2[i])

        if n1 > n2:                
            ans.extend(word1[n:])
        else:
            ans.extend(word2[n:])

        return ''.join(ans)    