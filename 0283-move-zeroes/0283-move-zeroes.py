from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        last_non_zero = 0  # 指向應該放非零元素的位置

        # 把所有非 0 元素往前放
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # 將剩下的位置補 0
        for i in range(last_non_zero, n):
            nums[i] = 0
