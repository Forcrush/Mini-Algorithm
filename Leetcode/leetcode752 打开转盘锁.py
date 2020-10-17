'''
Author: Puffrora
Date: 2020-10-16 15:04:29
LastModifiedBy: Puffrora
LastEditTime: 2020-10-16 15:48:44
'''


class Solution:
    def openLock(self, deadends, target):

        queue = [('0000', 0)]
        seen = {'0000'}
        while queue:
            num, depth = queue.pop(0)
            if num == target: return depth
            if num in deadends: continue
            for i in range(len(num)):
                for j in [-1, 1]:
                    tmp = str((int(num[i]) + j) % 10)
                    next_num = num[:i] + tmp + num[i+1:]
                    if next_num not in seen:
                        queue.append((next_num, depth+1))
                        seen.add(next_num)

        return -1


