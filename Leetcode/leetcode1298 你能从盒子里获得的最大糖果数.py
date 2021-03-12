'''
Author: Puffrora
Date: 2021-03-12 15:17:30
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 16:00:58
'''


from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        from collections import deque

        queue = deque()
        total_candies = 0
        current_keys = set()
        unopen_box = set()
        for b in initialBoxes:
            if status[b]:
                queue.append(b)
            else:
                unopen_box.add(b)
        
        while queue:
            for _ in range(len(queue)):
                cur_box = queue.popleft()

                # 拆箱
                total_candies += candies[cur_box]
                for k in keys[cur_box]:
                    current_keys.add(k)
                for b in containedBoxes[cur_box]:
                    if status[b]:
                        queue.append(b)
                    else:
                        unopen_box.add(b)

                # 检查是否有钥匙可以打开上锁的盒子
                match = current_keys.intersection(unopen_box)
                for b in match:
                    current_keys.discard(b)
                    unopen_box.discard(b)
                    queue.append(b)
        
        return total_candies

