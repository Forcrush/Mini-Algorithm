'''
Author: Puffrora
Date: 2021-01-26 19:52:11
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 19:58:38
'''


class Solution:
    def numOfBurgers(self, tomatoSlices, cheeseSlices):

        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2

        if x >= 0 and y >= 0:
            if x - int(x) == 0 and y - int(y) == 0:
                return [int(x), int(y)]
        return []
