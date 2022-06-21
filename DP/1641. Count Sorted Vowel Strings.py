class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5
        #if n == 2: return 
        dp = [[]]*(n+1)
        dp[1] = [1, 1, 1, 1, 1]
        dp[2] = [5, 4, 3, 2, 1]
        
        for i in range(3, n+1):
            dp[i] = [sum(dp[i-1][0:]), sum(dp[i-1][1:]), sum(dp[i-1][2:]), sum(dp[i-1][3:]), sum(dp[i-1][4:])]
        print(dp)
        return sum(dp[-1])
        
        