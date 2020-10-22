'''
Author: Puffrora
Date: 2020-10-22 09:45:48
LastModifiedBy: Puffrora
LastEditTime: 2020-10-22 10:29:48
'''


class Solution:
    def updateBoard(self, board, click):

        def neighbor(x, y):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx or dy) and (0 <= x+dx < len(board) and 0 <= y+dy < len(board[0])):
                        yield x+dx, y+dy

        def get_mine_around(x, y):
            res = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx or dy) and (0 <= x+dx < len(board) and 0 <= y+dy < len(board[0])):
                        res += board[x+dx][y+dy] == 'M'
            return res

        x, y = click

        # 点到地雷
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        # 点到已被揭露的方块
        if board[x][y] == 'B' or board[x][y].isdigit():
            return board

        # 点到未被揭露的方块 board[x][y] == 'E'
        # 如果此方块周围有雷
        mines = get_mine_around(x, y)
        if mines:
            board[x][y] = str(mines)
            return board
        # 此方块周围无雷 队列中都是周围无雷的方块
        queue = [(x, y)]
        while queue:
            curx, cury = queue.pop(0)
            board[curx][cury] = 'B'
            for nx, ny in neighbor(curx, cury):
                if board[nx][ny] == 'E':
                    mines = get_mine_around(nx, ny)
                    # 有雷 揭示此方块并不再搜索此方块
                    if mines:
                        board[nx][ny] = str(mines)
                    # 周围没有地雷 可以继续搜索此方块
                    else:
                        board[nx][ny] = 'B'
                        queue.append((nx, ny))

        return board

