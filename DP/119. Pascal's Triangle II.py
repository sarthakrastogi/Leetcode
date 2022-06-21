class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 1: return [1]
        rows = [[]]*(rowIndex+1)
        rows[0] = [1]
        rows[1] = [1, 1]
        
        for i in range(2, rowIndex+1):
            print(rows)
            
            rows[i] = [1] + [rows[i-1][j] + rows[i-1][j+1] for j in range(0, len(rows[i-1])-1)] + [1]
            
        
        return rows[-1]