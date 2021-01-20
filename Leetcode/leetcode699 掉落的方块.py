'''
Author: Puffrora
Date: 2021-01-18 21:29:30
LastModifiedBy: Puffrora
LastEditTime: 2021-01-18 22:02:53
'''


# 线段树
# 时间复杂度 O(NlogN)
# 空间复杂度 O(N)
# https://leetcode-cn.com/problems/falling-squares/solution/cong-xian-duan-shu-dao-tu-lun-jian-mo-by-wotxdx/
class Solution:
    def fallingSquares(self, positions):

        class Node:
            def __init__(self, l, r, h, maxR):
                # l r h 为此节点区间维护的左右边界和这个区间的最大高度
                self.l = l
                self.r = r
                self.h = h
                # maxR 为此节点维护的最大右边界
                self.maxR = maxR

                self.left = None
                self.right = None

        # 插入新区间节点
        def insert(root, l, r, h):
            if root == None:
                return Node(l, r, h, r)

            if l <= root.l:
                root.left = insert(root.left, l, r, h)
            else:
                root.right = insert(root.right, l, r, h)

            # 需要根节点更新 maxR
            root.maxR = max(root.maxR, r)
            return root

        # 查询区间最大高度
        def query(root, l, r):
            # 新节点的左边界大于等于目前的maxH
            if root == None or l >= root.maxR:
                return 0

            curH = 0
            # 跟root节点代表的区间相交
            if not (r <= root.l or root.r <= l):
                curH = root.h

            curH = max(curH, query(root.left, l, r))
            # 剪枝
            if r > root.l:
                curH = max(curH, query(root.right, l, r))
            return curH

        res = []
        root = None
        maxH = 0

        for l, side in positions:
            r = l + side
            
            # l-r 区间的最高高度
            curH = query(root, l, r)
            # 方块掉落 树中插入新区间节点
            root = insert(root, l, r, curH+side)

            maxH = max(maxH, curH+side)
            res.append(maxH)
        
        return res

