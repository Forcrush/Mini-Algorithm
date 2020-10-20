'''
Author: Puffrora
Date: 2020-10-20 17:35:59
LastModifiedBy: Puffrora
LastEditTime: 2020-10-20 17:59:58
'''
class Solution:
    def isBipartite(self, graph):

        # 1 / -1 分别表示节点属于的两个集合
        visited = [0] * len(graph)


        for i in range(len(graph)):
            if not visited[i]:
                queue = [i]
                visited[i] = 1
                while queue:
                    top = queue.pop(0)
                    cur_set = visited[top]
                    for child in graph[top]:
                        if visited[child] == 0:
                            visited[child] = -cur_set
                            queue.append(child)
                        elif visited[child] == cur_set:
                            return False
                        # child 分类正确且已经被访问过
                        else:
                            continue
                
        return True
