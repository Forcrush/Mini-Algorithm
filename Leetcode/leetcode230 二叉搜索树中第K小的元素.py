# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-07 17:04:44
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-07 17:13:53


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 二叉搜索树 中序遍历 找到第k大元素
# 递归
class Solution:
	def kthSmallest(self, root, k):

		def midOrder(root):
			if not root:
				return []
			return midOrder(root.left) + [root.val] + midOrder(root.right)

		return midOrder(root)[k-1]


# 迭代
class Solution2:
	def kthSmallest(self, root, k):

		stack = []
		
		while True:
			while root:
				stack.append(root)
				root = root.left
			node = stack.pop()
			k -= 1
			if k == 0:
				return node.val
			root = node.right