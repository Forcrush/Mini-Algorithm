# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 23:53:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 23:54:42


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def postorderTraversal(self, root):
		if not root: return []

		res = []
		def postorder(r):
			if not r: return
			postorder(r.left)
			postorder(r.right)
			res.append(r.val)

		postorder(root)
		return res