```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)       

        left, right = 0, size -1 #以陣列的格子去看

        while left <= right:
            mid = left + (right - left) //2 #假如說陣列是5 4//2=2 mid = 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 #在右區間尋找
            else:
                right = mid - 1 #在左區間尋找'

    return left #如果找不到target值就把它插入在這格
```
