'''
Author: Puffrora
Date: 2020-10-10 21:52:53
LastModifiedBy: Puffrora
LastEditTime: 2020-10-10 22:23:55
'''


class Solution:
    def validSquare(self, p1, p2, p3, p4):

        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            
        p = [p1, p2, p3, p4]
        p.sort(key=lambda x: (x[0], x[1]))
        
        if dist(p[0], p[1]) != 0 and dist(p[0], p[1]) == dist(p[1], p[3]) and dist(p[1], p[3]) == dist(p[3], p[2]) and dist(p[3], p[2]) == dist(p[2], p[0]) and dist(p[0], p[3]) == dist(p[1], p[2]):
            return True

        return False

