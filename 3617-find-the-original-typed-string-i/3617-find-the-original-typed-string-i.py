class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1  # 本身就是原始字串的情況

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1

        return count