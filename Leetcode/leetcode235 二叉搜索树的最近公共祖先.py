# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-07 00:28:22
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-07 00:39:51


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# recursion
class Solution:
	def lowestCommonAncestor(self, root, p, q):
		
		if p.val < root.val and q.val < root.val:
			return self.lowestCommonAncestor(root.left, p, q)
		elif p.val > root.val and q.val > root.val:
			return self.lowestCommonAncestor(root.right, p, q)
		else:
			return root


# iteration
class Solution:
	def lowestCommonAncestor(self, root, p, q):
		
		node = root

		while node:
			if p.val < node.val and q.val < node.val:
				node = node.left
			elif p.val > node.val and q.val > node.val:
				node = node.right
			else:
				return node