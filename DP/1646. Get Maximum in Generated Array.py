class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1: return n
            
        nums = [0]*(n+1)
        nums[0] = 0
        nums[1] = 1
        
        for i in range(2, len(nums)):
            if i%2 == 0:
                nums[i] = nums[i//2]
            
            else:
                nums[i] = nums[(i-1)//2] + nums[(i+1)//2]
        
        return max(nums)
        
        