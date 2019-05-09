class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        else:
            res = []
            for _ in range(n):
                res.append([0]*n)
            rowbegin = 0
            colend = n - 1
            rowend = n - 1
            colbegin = 0
            num = 1
            while num <= n**2:

                for i in range(colbegin, colend + 1):
                    res[rowbegin][i] = num
                    num += 1
                rowbegin += 1

                for i in range(rowbegin, rowend + 1):
                    res[i][colend] = num
                    num += 1
                colend -= 1

                for i in range(colend, colbegin - 1, -1):
                    res[rowend][i] = num
                    num +=1
                rowend -= 1

                for i in range(rowend, rowbegin - 1, -1):
                    res[i][colbegin] = num
                    num += 1
                colbegin += 1
                
        return res