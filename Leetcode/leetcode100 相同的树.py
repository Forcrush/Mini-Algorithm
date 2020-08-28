# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-12 11:48:28
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-12 11:48:42


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        # p and q both None
        if not p and not q:
            return True
        # one of p and q is None
        elif not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)