class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(num, num+dp[i-1])
        return max(dp)