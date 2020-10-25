'''
Author: Puffrora
Date: 2020-10-25 17:16:24
LastModifiedBy: Puffrora
LastEditTime: 2020-10-25 17:46:30
'''


"""
blocked 能封锁的 最多坐标数是 (len(blocked) * (len(blocked)-1)) // 2, 
如果从 source --> target 能走的步数大于这个数, 
或者从 target --> source 能走的步数大于这个数,  则True   

BFS 搜索 source 和 target

"""
class Solution:
    def isEscapePossible(self, blocked, source, target):

        def neighbor(cx, cy):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= cx+dx < 10**6 and 0 <= cy+dy < 10**6:
                    yield cx+dx, cy+dy

        def BFS(src, tar):
            max_step = (len(blocked) * (len(blocked) - 1)) // 2
            queue = [(src[0], src[1])]
            visited = set()
            visited.add(tuple(src))
            
            while queue:
                cur_x, cur_y = queue.pop(0)
                if len(visited) > max_step or (cur_x, cur_y) == tuple(tar):
                    return True
                for nx, ny in neighbor(cur_x, cur_y):
                    if (nx, ny) not in visited and [nx, ny] not in blocked:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            
            return False
            
        return BFS(source, target) and BFS(target, source)


