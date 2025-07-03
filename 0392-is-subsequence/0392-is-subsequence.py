class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        #雙指針寫法，等一個通過在去找下一個，要看s裡面的順序
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
