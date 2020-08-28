# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-11 12:40:18
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-11 13:06:23


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 对于 n 个点生成的二叉搜索树数量等价于数学上第 n 个「卡特兰数」 用 G_n表示
# 时间复杂度 O(n*Gn)
class Solution:
	def generateTrees(self, n):

		def recursion_search(start, end):
			if start > end: return [None]
			res = []

			for i in range(start, end+1):
				left = recursion_search(start, i-1)
				right = recursion_search(i+1, end)

				for l in left:
					for r in right:
						newtree = TreeNode(i)
						newtree.left, newtree.right = l, r
						res.append(newtree)

			return res

		return recursion_search(1, n) if n else []