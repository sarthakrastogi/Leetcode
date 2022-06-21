class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        for i in range(1, len(nums)):
            cur_dp = 0
            for j in range(len(nums[:i])):
                if nums[j] < nums[i]:
                    if dp[j] > cur_dp: cur_dp = dp[j]
            dp[i] += cur_dp
            print(cur_dp)
            
        print(dp)
        return max(dp)
            
            
                        
                        
            
                