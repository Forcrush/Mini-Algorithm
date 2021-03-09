'''
Author: Puffrora
Date: 2021-03-09 12:49:41
LastModifiedBy: Puffrora
LastEditTime: 2021-03-09 13:27:18
'''


from typing import List


# 时间复杂度 O(N*N) N = len(quiet)
# 空间复杂度 O(N*N)
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        from collections import defaultdict

        rich = defaultdict(set)
        final_rich = defaultdict(set)
        for x, y in richer:
            rich[y].add(x)
        
        # 记忆化搜索所有大于 p 的节点
        def find_all_richer(p):
            cur = {p}
            if rich[p]:
                for n in rich[p]:
                    if final_rich[n]:
                        cur = cur.union(final_rich[n])
                    else:
                        cur = cur.union(find_all_richer(n))
            
            final_rich[p] = cur
            return final_rich[p]

        for person in range(len(quiet)):
            if not final_rich[person]:
                final_rich[person] = find_all_richer(person)
        
        # 寻找最小quiet
        res = [0 for _ in range(len(quiet))]
        for person in range(len(res)):
            res[person] = min(final_rich[person], key=lambda x: quiet[x])

        return res
