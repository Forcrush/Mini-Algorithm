'''
Author: Puffrora
Date: 2020-10-13 10:45:43
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 12:00:36
'''


class RangeModule:

    import bisect

    def __init__(self):
        self.range = []

    # 找到目标区间的起始下标和终止下标
    def get_bounds(self, left, right):
        i, j = 0, len(self.range) - 1
        for k in (100, 10, 1):
            while i + k - 1 < len(self.range) and self.range[i+k-1][1] < left:
                i += k
            while j - k + 1 >= 0 and self.range[j-k+1][0] > right:
                j -= k
        return i, j

    def addRange(self, left, right):
        i, j = self.get_bounds(left, right)
        if i <= j:
            left = min(self.range[i][0], left)
            right = max(self.range[j][1], right)
        
        self.range[i:j+1] = [(left, right)]

    def queryRange(self, left, right):
        i = bisect.bisect_left(self.range, (left, float('inf')))
        if i: i -= 1
        return bool(self.range) and self.range[i][0] <= left and self.range[i][1] >= right
    
    def removeRange(self, left, right):
        i, j = self.get_bounds(left, right)
        merge = []
        for k in range(i, j+1):
            if self.range[k][0] < left:
                merge.append((self.range[k][0], left))
            if right < self.range[k][1]:
                merge.append((right, self.range[k][1]))
        self.range[i:j+1] = merge

    # Your RangeModule object will be instantiated and called as such:
    # obj = RangeModule()
    # obj.addRange(left,right)
    # param_2 = obj.queryRange(left,right)
    # obj.removeRange(left,right)
