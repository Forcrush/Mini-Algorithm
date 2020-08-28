# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-18 20:40:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-18 23:34:53


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def rightSideView(self, root):

		if not root: return []

		res = []

		queue = [root]
		while queue:
			see = False
			for i in range(len(queue)):
				node = queue.pop(0)
				if node:
					if not see:
						see = True
						res.append(node.val)
					queue.append(node.right)
					queue.append(node.left)
		return res