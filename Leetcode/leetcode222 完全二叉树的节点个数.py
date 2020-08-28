# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 18:15:52
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 19:06:58


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 时间复杂度: O(d^2) = O(logN * logN) -- d 为树的高度, N 为所有节点数
# 空间复杂度: O(1)
class Solution:
	def countNodes(self, root):

		# 根结点算深度为 0 的树
		def count_depth(root):
			depth = 0
			while root:
				root = root.left
				depth += 1

			return depth-1

		def exist(idx, node, depth):
			"""
			Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
			Return True if last level node idx exists. 
			Binary search with O(d) complexity.
			"""
			left, right = 0, 2**depth - 1
			depth = count_depth(root)
			for _ in range(depth):
				mid = (left + right) // 2
				# idx在前半部分 向下搜寻左子树
				if idx <= mid:
					node = node.left
					right = mid
				# idx在后半部分 向下搜寻右子树
				else:
					node = node.right
					left = mid + 1

			return node is not None

		if not root: return 0

		depth = count_depth(root)
		if depth == 0: return 1

		# Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
		# Perform binary search to check how many nodes exist.
		left, right = 0, 2**depth-1
		while left <= right:
			mid = (left + right) // 2
			if exist(mid, root, depth):
				left = mid + 1
			else:
				right = mid - 1

		# The tree contains 2**d - 1 nodes on the first (d - 1) levels
		# and left nodes on the last level.
		return 2**depth - 1 + left

