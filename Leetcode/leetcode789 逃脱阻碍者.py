'''
Author: Puffrora
Date: 2021-02-28 21:34:46
LastModifiedBy: Puffrora
LastEditTime: 2021-02-28 21:38:28
'''


from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        def manhattan(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        return all (manhattan([0, 0], target) < manhattan(g, target) for g in ghosts)