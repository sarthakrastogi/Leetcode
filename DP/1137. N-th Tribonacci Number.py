class Solution:
    def tribonacci(self, n: int) -> int:
        
        d = {0:0, 1:1, 2:1}
        def tri(n):
            if n in d: return d[n]
            t = tri(n-1) + tri(n-2) + tri(n-3)
            d.update({n : t})
            return t
        return tri(n)