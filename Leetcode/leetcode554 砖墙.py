'''
Author: Puffrora
Date: 2020-10-11 17:09:38
LastModifiedBy: Puffrora
LastEditTime: 2020-10-11 17:31:52
'''


class Solution:
    def leastBricks(self, wall):
        from collections import defaultdict

        dic = defaultdict(int)
        row_width = sum(wall[0])
        common_width_num = 0

        for row in range(len(wall)):
            width = 0
            for block in wall[row]:
                width += block
                dic[width] += 1
                if width != row_width:
                    common_width_num = max(common_width_num, dic[width])
        
        return len(wall) - common_width_num


