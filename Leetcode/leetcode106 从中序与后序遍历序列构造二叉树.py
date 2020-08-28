# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 12:59:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 13:11:31


class Solution:
	def buildTree(self, inorder, postorder):

		def to_build(postorder_l, postorder_r, inorder_l, inorder_r):
			if postorder_l > postorder_r:
				return None

			# 后序遍历中的第一个节点就是根节点
			postorder_root = postorder_r
			# 在中序遍历中定位根节点
			inorder_root = memo[postorder[postorder_root]]

			# 先把根节点建立出来
			root = TreeNode(postorder[postorder_root])
			# 得到左子树中的节点数目
			left_subtree_size = inorder_root - inorder_l

			# 递归地构造左子树，并连接到根节点
			# 后序遍历中「从 左边界 开始的 size_left_subtree」个元素就
			# 对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
			root.left = to_build(postorder_l, postorder_l+left_subtree_size-1, inorder_l, inorder_root-1)
			
			# 递归地构造右子树，并连接到根节点
			# 后序遍历中「从 左边界+左子树节点数目 开始到 右边界-1」个元素就
			# 对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
			root.right = to_build(postorder_l+left_subtree_size, postorder_r-1, inorder_root+1, inorder_r)

			return root

		memo = {}
		for i in range(len(inorder)):
			memo[inorder[i]] = i

		return to_build(0, len(postorder)-1, 0, len(inorder)-1)