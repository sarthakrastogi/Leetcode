class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        
        curmin, curmax = 1, 1
        
        for n in nums:
            if n == 0: curmin, curmax = 1, 1
            else:
                tmp = curmin*n
                curmin = min(n*curmin, n*curmax, n)
                curmax = max(tmp, n*curmax, n)
                res = max(res, curmax)
            
        return res