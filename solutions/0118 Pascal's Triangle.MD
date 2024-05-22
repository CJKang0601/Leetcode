
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tr =[[0] * i for i in range(1, numRows+1)]#先製造出一個三角每一列作出奇數
        
        for i in range(numRows):
            tr[i][0] = 1 #每一列最前面和最後一個都會是1
            tr[i][i] = 1
        
        res = []
        for i in range(numRows): #創造一個內三角形
            for j in range(i):
                if i != 0 and j != 0:
                    tr[i][j] = tr[i-1][j-1]+ tr[i-1][j] 
                
            res.append(tr[i])

        return res
```
