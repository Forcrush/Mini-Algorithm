# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 11:44:42
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 12:59:15


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def buildTree(self, preorder, inorder):

		def to_build(preorder_l, preorder_r, inorder_l, inorder_r):
			if preorder_l > preorder_r:
				return None

			# 前序遍历中的第一个节点就是根节点
			preorder_root = preorder_l
			# 在中序遍历中定位根节点
			inorder_root = memo[preorder[preorder_root]]

			# 先把根节点建立出来
			root = TreeNode(preorder[preorder_root])
			# 得到左子树中的节点数目
			left_subtree_size = inorder_root - inorder_l

			# 递归地构造左子树，并连接到根节点
			# 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就
			# 对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
			root.left = to_build(preorder_l+1, preorder_l+left_subtree_size, inorder_l, inorder_root-1)
			
			# 递归地构造右子树，并连接到根节点
			# 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」个元素就
			# 对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
			root.right = to_build(preorder_l+1+left_subtree_size, preorder_r, inorder_root+1, inorder_r)

			return root

		memo = {}
		for i in range(len(inorder)):
			memo[inorder[i]] = i

		return to_build(0, len(preorder)-1, 0, len(inorder)-1)