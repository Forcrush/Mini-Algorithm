'''
Author: Puffrora
Date: 2021-01-21 13:35:39
LastModifiedBy: Puffrora
LastEditTime: 2021-01-21 15:33:34
'''


# 扫描线法
# 时间复杂度 O(N*N*logN)
# 空间复杂度 O(N)
class Solution:
    def rectangleArea(self, rectangles):
        sweep_line = []
        for x1, y1, x2, y2 in rectangles:
            # 1 代表添加 y1 这跟水平线 ; 0 代表 删除 y2 这条水平线
            sweep_line.append((y1, 1, x1, x2))
            sweep_line.append((y2, 0, x1, x2))
        sweep_line.sort()

        res = 0
        cur_horizontal_range = []
        last_y = sweep_line[0][0]

        # 获取同一水平线上的区间长度和
        def get_all_horizontal_range():
            range_sum = 0
            cur = -1
            for x1, x2 in cur_horizontal_range:
                cur = max(cur, x1)
                range_sum += max(0, x2-cur)
                cur = max(cur, x2)
            return range_sum

        for y, flag, x1, x2 in sweep_line:
            res += get_all_horizontal_range() * (y - last_y)

            # add the line
            if flag:
                cur_horizontal_range.append((x1, x2))
                cur_horizontal_range.sort()
            # delete the line
            else:
                cur_horizontal_range.remove((x1, x2))
            
            last_y = y

        return res % (10 ** 9 + 7)


# 线段树
# 时间复杂度 O(N*logN)
# 空间复杂度 O(N)
class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left
    
    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end)
        return self._right

    def update(self, x1, x2, val):
        if x1 >= x2: return 0
        if self.start == x1 and self.end == x2:
            self.count += val
        else:
            self.left.update(x1, min(self.mid, x2), val)
            self.right.update(max(self.mid, x1), x2, val)
        
        if self.count > 0:
            self.total = X[self.end] - X[self.start]
        else:
            self.total = self.left.total + self.right.total
        
        return self.total


class Solution1:
    def rectangleArea(self, rectangles):
        sweep_line = []
        global X
        X = set()
        for x1, y1, x2, y2 in rectangles:
            # ! 线段树法需跳过此种情况
            if x1 == x2: continue
            # 1 代表添加 y1 这跟水平线 ; -1 代表 删除 y2 这条水平线
            sweep_line.append((y1, 1, x1, x2))
            sweep_line.append((y2, -1, x1, x2))
            X.add(x1)
            X.add(x2)
        sweep_line.sort()
        X = sorted(X)
        X_i = {x:i for i, x in enumerate(X)}

        segment_tree = Node(0, len(X)-1)
        res = cur_x_xum = 0
        last_y = sweep_line[0][0]

        for y, val, x1, x2 in sweep_line:
            res += cur_x_xum * (y - last_y)
            cur_x_xum = segment_tree.update(X_i[x1], X_i[x2], val)
            last_y = y

        return res % (10 ** 9 + 7)


# print(Solution().rectangleArea([[4, 1, 8, 5], [1, 4, 5, 8], [4, 7, 8, 11], [7, 4, 11, 8]]))
# print(Solution1().rectangleArea([[4, 1, 8, 5], [1, 4, 5, 8], [4, 7, 8, 11], [7, 4, 11, 8]]))
# print(Solution().rectangleArea([[471, 0, 947, 999], [166, 0, 166, 320]]))
# print(Solution1().rectangleArea([[471, 0, 947, 999], [166, 0, 166, 320]]))
