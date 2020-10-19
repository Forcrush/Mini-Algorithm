'''
Author: Puffrora
Date: 2020-10-19 12:21:30
LastModifiedBy: Puffrora
LastEditTime: 2020-10-19 12:30:13
'''


"""
将车辆按照起始位置降序排序后，我们顺序扫描这些车辆。如果相邻的两辆车，
前者比后者行驶到终点需要的时间短，那么后者永远追不上前者，即从后者开
始的若干辆车辆会组成一个新的车队；如果前者不比后者行驶到终点需要的时
间短，那么后者可以在终点前追上前者，并和前者形成车队。此时我们将后者
到达终点的时间置为前者到达终点的时间。
"""
class Solution:
    def carFleet(self, target, position, speed):

        if not position or not speed:
            return 0

        cars = sorted(zip(position, speed))
        time = [(target - p) / s for p, s in cars]
        res = 0

        while len(time) > 1:
            top = time.pop()
            if top < time[-1]:
                res += 1
            else:
                time[-1] = top

        return res + 1
