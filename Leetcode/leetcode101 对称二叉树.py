# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 13:43:52
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 13:50:48


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isSymmetric(self, root):

		def checkSym(left, right):
			if not left and not right:
				return True
			if left and not right: return False
			if right and not left: return False
			if left.val == right.val:
				return checkSym(left.right, right.left) and checkSym(left.left, right.right)
			return False

		return checkSym(root.left, root.right) if root else True