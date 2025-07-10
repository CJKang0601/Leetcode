class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        
        # 計算左側最大間隔（前綴最大間隔）
        left_gaps = [0] * n
        left_gaps[0] = startTime[0]  # 從事件開始到第一個會議
        for i in range(1, n):
            # 左側最大間隔 = max(之前的最大間隔, 當前會議前的間隔)
            left_gaps[i] = max(left_gaps[i-1], startTime[i] - endTime[i-1])
        
        # 計算右側最大間隔（後綴最大間隔）
        right_gaps = [0] * n
        right_gaps[n-1] = eventTime - endTime[n-1]  # 從最後會議到事件結束
        for i in range(n-2, -1, -1):
            # 右側最大間隔 = max(之後的最大間隔, 當前會議後的間隔)
            right_gaps[i] = max(right_gaps[i+1], startTime[i+1] - endTime[i])
        
        max_free = 0
        
        # 嘗試移動每個會議
        for i in range(n):
            duration = endTime[i] - startTime[i]
            
            # 計算移除會議i後，左右兩側的直接間隔
            left_gap = startTime[i] - (endTime[i-1] if i > 0 else 0)
            right_gap = (startTime[i+1] if i < n-1 else eventTime) - endTime[i]
            
            # 如果可以將會議i插入到左側或右側的某個間隔中
            interval = 0
            if (i > 0 and left_gaps[i-1] >= duration) or \
               (i < n-1 and right_gaps[i+1] >= duration):
                interval = duration
            
            # 移除會議i後能獲得的最大空閒時間
            # = 左側間隔 + 會議時長（如果可以插入其他地方）+ 右側間隔
            max_free = max(max_free, left_gap + interval + right_gap)
        
        return max_free