class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = sum(nums) % k
        return answer 
        