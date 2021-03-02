'''
Author: Puffrora
Date: 2021-03-02 12:18:30
LastModifiedBy: Puffrora
LastEditTime: 2021-03-02 12:49:15
'''


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        have = set()

        def dfs(cur, letters):
            for i in range(len(letters)):
                next_c = letters.pop(i)
                have.add(cur+next_c)
                dfs(cur+next_c, letters)

                letters.insert(i, next_c)
        
        dfs('', list(tiles))

        return len(have)

