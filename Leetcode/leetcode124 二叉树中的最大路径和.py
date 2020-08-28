# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-09 00:26:30
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-09 00:34:06


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def maxPathSum(self, root):

		global path_sum
		path_sum = float("-inf")

		def backtracking(r):
			global path_sum
			if not r: return 0

			l_contri, r_contri = max(backtracking(r.left), 0), max(backtracking(r.right), 0)
			path_sum = max(path_sum, r.val+l_contri+r_contri)

			return r.val + max(l_contri, r_contri)

		backtracking(root)

		return path_sum