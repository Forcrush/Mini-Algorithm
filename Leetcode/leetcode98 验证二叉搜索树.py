# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-11 13:31:39
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-11 13:46:35


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isValidBST(self, root):

		def bound_check(r, lower, upper):
			if not r: return True

			if r.val <= lower or r.val >= upper:
				return False

			if bound_check(r.left, lower, r.val) and bound_check(r.right, r.val, upper):
				return True

			return False

		return bound_check(root, float("-inf"), float("inf"))