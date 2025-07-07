class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # 先根據 startDay 排序
        event_id = 0
        total_days = max(end for _, end in events)  # 找出最後一天
        min_heap = []
        attended = 0

        for day in range(1, total_days + 1):
            # 加入所有今天開始的活動
            while event_id < len(events) and events[event_id][0] == day:
                heapq.heappush(min_heap, events[event_id][1])  # 只記 endDay
                event_id += 1

            # 清掉所有已經過期的活動
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # 今天可以參加一場活動
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

        return attended