'''
Author: Puffrora
Date: 2021-01-27 19:43:02
LastModifiedBy: Puffrora
LastEditTime: 2021-01-27 19:59:01
'''


class Solution:
    def movesToChessboard(self, board):
        
        n = len(board)


        # 任意的 board 的四角都必须要是这三种情况：四个0，四个1，两个0两个1.
        # 因为 board 只能交换行和列，所以这四个角两两是绑定在一起的
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[0][j] ^ board[i][0] ^ board[i][j]:
                    return -1


        # row, col 表示在某一行，某一列中1的个数是多少
        row = col = 0
        # misrow, miscol 表示某一行，某一列中错位的值的个数是多少
        misrow = miscol = 0

        for i in range(n):
            row += board[0][i]
            col += board[i][0]
            misrow += board[0][i] != i % 2
            miscol += board[i][0] != i % 2
        
        if row < n // 2 or row > (n + 1) // 2: return -1
        if col < n // 2 or col > (n + 1) // 2: return -1
        
        # 总错位数
        # 下面 misrow, n-misrow 考虑了目标是 010101 或 101010 两种情况
        misplace_num = 0

        # n 是奇数
        if n % 2:
            if misrow % 2:
                misrow = n - misrow
            if miscol % 2:
                miscol = n - miscol
            misplace_num = misrow + miscol
        # n 是偶数
        else:
            misplace_num += min(misrow, n-misrow)
            misplace_num += min(miscol, n-miscol)

        return misplace_num // 2
