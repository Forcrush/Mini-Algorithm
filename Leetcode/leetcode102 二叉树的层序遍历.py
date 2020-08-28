# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 23:54:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 00:01:12


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def levelOrder(self, root):

		import collections
		deque = collections.deque()
		deque.append(root)
		res = []
		while deque:
			size = len(deque)
			level = []
			for _ in range(size):
				cur = deque.popleft()
				if not cur:
					continue
				level.append(cur.val)
				deque.append(cur.left)
				deque.append(cur.right)
			if level:
				res.append(level)
		return res
