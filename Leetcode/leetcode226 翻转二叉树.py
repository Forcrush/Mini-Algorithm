# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 19:08:00
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 19:12:16


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def invertTree(self, root):

		if root:
			iv_left = self.invertTree(root.left)
			iv_right = self.invertTree(root.right)
			root.right = iv_left
			root.left = iv_right
			return root
		else:
			return None
