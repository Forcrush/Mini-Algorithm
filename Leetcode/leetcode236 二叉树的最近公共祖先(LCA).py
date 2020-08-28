# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-07 00:40:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-07 09:42:20


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def lowestCommonAncestor(self, root, p, q):

		# root == None
		if not root: return root
		
		# root为其中一个结点 则不管另一个在左子树或右子树 LCA就是root
		if root.val == p.val or root.val == q.val:
			return root

		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)

		# p,q 分布在左右子树 LCA就是root
		if left and right:
			return root
		if left:
			return left
		if right:
			return right
		return None