class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            pascal.append([1]+ [pascal[i-1][j] + pascal[i-1][j+1] for j in range(len(pascal[i-1])-1)] + [1])
            #print(pascal)
          
        return pascal