class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # t = 0 是事件開始的時候, t = evenTime 是時間結束的時候

        s = 0
        pre = 0
        res = 0
        for index in range(k):
            s += endTime[index] - startTime[index]
        
        for index in range(k, len(startTime)):
            res = max(res, startTime[index] - pre - s)
            s -= (endTime[index - k] - startTime[index - k])
            s += (endTime[index] - startTime[index])
            pre = endTime[index - k]
        
        res = max(res, eventTime - pre - s)
        return res