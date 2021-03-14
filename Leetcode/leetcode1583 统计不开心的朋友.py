'''
Author: Puffrora
Date: 2021-03-13 20:07:34
LastModifiedBy: Puffrora
LastEditTime: 2021-03-13 20:19:12
'''


from typing import List


# 时间复杂度 O(n^2)
# 空间复杂度 O(n^2)
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        rank = [[0 for _ in range(n)] for _ in range(n)]

        for i, p in enumerate(preferences):
            r = n-1
            for j in p:
                rank[i][j] = r
                r -= 1
        
        pair_dic = {}
        for x, y in pairs:
            pair_dic[x] = y
            pair_dic[y] = x
        
        unhappy = set()
        for person in range(n):
            for friend in range(n):
                if rank[person][friend] > rank[person][pair_dic[person]] and \
                    rank[friend][person] > rank[friend][pair_dic[friend]]:
                    unhappy.add(person)
                    unhappy.add(friend)

        return len(unhappy)

