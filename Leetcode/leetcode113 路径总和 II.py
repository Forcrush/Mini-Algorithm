# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-13 00:37:04
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-13 00:48:24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def pathSum(self, root, sum):

		def recur_search(r, cur_sum, path):

			# 叶节点
			if not r.left and not r.right:
				if cur_sum + r.val == sum:
					res.append(path + [r.val])

			if r.left:
				recur_search(r.left, cur_sum+r.val, path+[r.val])
			if r.right:
				recur_search(r.right, cur_sum+r.val, path+[r.val])

		if not root: return []

		res = []
		recur_search(root, 0, [])

		return res


# 内存优化版本 
class Solution:
	def pathSum(self, root, sum):

		def recur_search(r, cur_sum, path):

			# 叶节点
			if not r.left and not r.right:
				if cur_sum + r.val == sum:
					res.append(path + [r.val])

			path.append(r.val)

			if r.left:
				recur_search(r.left, cur_sum+r.val, path)
			if r.right:
				recur_search(r.right, cur_sum+r.val, path)

			path.pop()

		if not root: return []

		res = []
		recur_search(root, 0, [])

		return res