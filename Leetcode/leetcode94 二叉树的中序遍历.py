# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 23:47:31
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 23:50:23


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def inorderTraversal(self, root):
		if not root: return []

		res = []
		def inorder(r):
			if not r: return
			inorder(r.left)
			res.append(r.val)
			inorder(r.right)

		inorder(root)
		return res