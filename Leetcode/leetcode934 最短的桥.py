'''
Author: Puffrora
Date: 2021-01-01 20:56:39
LastModifiedBy: Puffrora
LastEditTime: 2021-01-01 21:21:32
'''


class Solution:
    def shortestBridge(self, A):

        row, col = len(A), len(A[0])

        def neighbor(i, j):
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= i+dx < row and 0 <= j+dy < col:
                    yield i+dx, j+dy

        def dfs(i, j):
            A[i][j] = 2
            for nx, ny in neighbor(i, j):
                if A[nx][ny] == 1:
                    dfs(nx, ny)

        found = False
        for i in range(row):
            for j in range(col):
                # DFS 标记出这座岛
                if A[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        print(A)
        # 随便找出一座岛进行 BFS
        flag = 0
        bridge = 0
        queue = []
        for i in range(row):
            for j in range(col):
                if A[i][j] and not flag:
                    flag = A[i][j]
                    queue.append((i, j))
                if flag and A[i][j] == flag:
                    queue.append((i, j))
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for nx, ny in neighbor(x, y):
                    if A[nx][ny] and A[nx][ny] != flag:
                        return bridge
                    elif not A[nx][ny]:
                        A[nx][ny] = flag
                        queue.append((nx, ny))
            bridge += 1
        
        return bridge


