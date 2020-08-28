# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 23:50:43
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 23:53:24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def preorderTraversal(self, root):
		if not root: return []

		res = []
		def preorder(r):
			if not r: return
			res.append(r.val)
			preorder(r.left)
			preorder(r.right)

		preorder(root)
		return res