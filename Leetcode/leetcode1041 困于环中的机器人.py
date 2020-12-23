'''
Author: Puffrora
Date: 2020-12-23 22:26:24
LastModifiedBy: Puffrora
LastEditTime: 2020-12-23 22:36:13
'''


"""
只考虑一轮后的起点和终点
1.假设一轮后起点和终点重合，那么下一次的每一轮执行后，都必将回到起点，true
2.假设一轮后起点和终点不重合，但方向终点和起点一致，那必将一条路走到黑了，false
3.假设一轮后起点和终点不重合，但方向终点和起点不一致，无论经过几轮也必将回到起点，true
"""
class Solution:
    def isRobotBounded(self, instructions):
        start = [0, 0]
        direction = 90
        for c in instructions:
            if c == 'L':
                direction = (direction + 90) % 360
            elif c == 'R':
                direction = (direction - 90) % 360
            elif c == 'G':
                if direction == 0:
                    start[0] += 1
                elif direction == 90:
                    start[1] += 1
                elif direction == 180:
                    start[0] -= 1
                elif direction == 270:
                    start[1] -= 1
        
        if start == [0, 0]:
            return True
        elif direction != 90:
            return True
        return False
