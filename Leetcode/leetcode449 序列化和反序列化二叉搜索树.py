# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 13:13:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 13:16:00


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1. 层次遍历 二叉树通用 leetcode297
class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		if not root: return ""

		import collections
		deque = collections.deque()
		deque.append(root)
		res = []
		while deque:
			node = deque.popleft()
			if node:
				res.append(str(node.val))
				deque.append(node.left)
				deque.append(node.right)
			else:
				res.append("null")

		return " ".join(res)

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		if not data: return None

		import collections
		deque = collections.deque()
		val = data.split()
		root = TreeNode(int(val[0]))
		deque.append(root)
		index = 1
		while deque:
			node = deque.popleft()
			if val[index] != "null":
				node.left = TreeNode(int(val[index]))
				deque.append(node.left)
			index += 1
			if val[index] != "null":
				node.right = TreeNode(int(val[index]))
				deque.append(node.right)
			index += 1

		return root

# 2. 对于二叉搜索树 其中序遍历是有序的
# 可以直接找到前序或后序遍历 排序得到中序遍历
# 再通过前序/后序 和 中序 构建二叉树

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))