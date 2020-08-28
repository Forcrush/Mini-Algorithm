# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 22:13:15
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 22:17:39


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def sumNumbers(self, root):

		def get_sum(node, cur_sum):
			if not node: return 0

			new_val = cur_sum * 10 + node.val
			# 叶子节点
			if not node.left and not node.right:
				return new_val
			# 非叶子节点
			else:
				return get_sum(node.left, new_val) + get_sum(node.right, new_val)
		
		return get_sum(root, 0)