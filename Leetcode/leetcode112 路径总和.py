# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-13 00:23:50
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-13 00:35:17


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def hasPathSum(self, root, sum):

		def recur_search(r, cur_sum):

			if r.left and r.right:
				return recur_search(r.left, cur_sum+r.val) or recur_search(r.right, cur_sum+r.val)
			elif r.left:
				return recur_search(r.left, cur_sum+r.val)
			elif r.right:
				return recur_search(r.right, cur_sum+r.val)
			else:
				return cur_sum + r.val == sum

		if not root: return False

		return recur_search(root, 0)