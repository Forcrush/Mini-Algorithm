'''
Author: Puffrora
Date: 2020-10-27 14:59:22
LastModifiedBy: Puffrora
LastEditTime: 2020-10-27 15:14:58
'''


class Solution:
    def maxDistToClosest(self, seats):
        left, right = 0, len(seats) - 1

        while left < len(seats):
            if seats[left] == 0:
                left += 1
            else:
                break
        while right >= 0:
            if seats[right] == 0:
                right -= 1
            else:
                break

        res = max(left, len(seats)-right-1)

        pre = left
        left += 1
        while left <= right:
            if seats[left] == 1:
                res = max(res, ((left - pre - 1) - 1) // 2 + 1)
                pre = left
            left += 1

        return res


