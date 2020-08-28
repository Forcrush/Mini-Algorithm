# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-03-06 12:31:28
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-03-06 13:00:14


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def rob(self, root):
		# 记忆化 解决重复子问题
		dic = {}

		def subrob(subroot):
			print(subroot)
			if subroot == None: return 0
			if subroot in dic: return dic[subroot]

			# 偷当前节点
			rob_root = subroot.val
			if subroot.left != None:
				rob_root += subrob(subroot.left.left) + subrob(subroot.left.right)
			if subroot.right != None:
				rob_root += subrob(subroot.right.left) + subrob(subroot.right.right)		
			
			# 不偷当前节点
			not_rob_root = subrob(subroot.left) + subrob(subroot.right)

			result = max(rob_root, not_rob_root)
			dic[subroot] = result

			return result

		return subrob(root)


# 我们使用一个大小为2的数组来表示一个节点状态 [0]代表不偷 [1]代表偷
# root[0] = Math.max(rob(root.left)[0], rob(root.left)[1]) + Math.max(rob(root.right)[0], rob(root.right)[1])
# root[1] = rob(root.left)[0] + rob(root.right)[0] + root.val
class Solution2:
	def rob(self, root):

		def subrob(root):
			if not root: return [0] * 2;
			left, right = subrob(root.left), subrob(root.right)
			# 偷当前节点
			rob_root = left[0] + right[0] + root.val
			# 不偷当前节点
			not_rob_root = max(left) + max(right)
			return [not_rob_root, rob_root]

		return max(subrob(root))

