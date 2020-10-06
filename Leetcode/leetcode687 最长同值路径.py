# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-19 15:17:41
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-19 16:06:09


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def longestUnivaluePath(self, root):

		if not root: return 0

		global res
		res = 0

		def search(node):
			global res
			if node == None:
				return 0

			left_tmp = search(node.left)
			right_tmp = search(node.right)

			left_contribution = left_tmp if node.left and node.left.val == node.val else 0
			right_contribution = right_tmp if node.right and node.right.val == node.val else 0

			res = max(res, left_contribution+right_contribution+1)

			return 1 + max(left_contribution, right_contribution)

		search(root)

		return res - 1