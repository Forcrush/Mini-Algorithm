'''
Author: Puffrora
Date: 2021-03-09 13:59:06
LastModifiedBy: Puffrora
LastEditTime: 2021-03-09 15:31:03
'''


from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        from collections import defaultdict

        if N == 1: return 1
        if not trust: return -1
        
        person = defaultdict(dict)
        all_trust = []
        for i, v in enumerate(trust):
            a, b = v
            # 1 represents outdegree 
            # 0 represents indegree
            if person[a].get(1) != None:
                person[a][1] += 1
            else:
                person[a][1] = 1
            
            if person[b].get(0) != None:
                person[b][0] += 1
            else:
                person[b][0] = 1

            if i >= N-2:
                if person[b][0] == N - 1:
                    all_trust.append(b)
        
        # 没有人可以获得所有人的信任
        if not all_trust:
            return -1

        for n in all_trust:
            # 这个人信任其他人
            if 1 in person[n] and person[n][1] > 0:
                continue
            # 这个人不信任任何人
            else:
                return n
        
        return -1
