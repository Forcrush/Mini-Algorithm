# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-11 13:47:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-13 00:14:51


# 对于二叉搜索树其中序遍历是有序的 如果两个节点发生交换则在中序遍历中存在点 a_i > a_i+1
# 注意如果是相邻点交换 则只存在一个点符合 a_i > a_i+1 否则会存在两个点满足 a_i > a_i+1

# 隐式中序遍历
# 时间复杂度 O(N)
# 空间复杂度 O(logN) 储存节点的栈高取决于树高

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def recoverTree(self, root):
		"""
		Do not return anything, modify root in-place instead.
		"""

		stack = []
		# 记录需要交换的两个点
		x, y = None, None
		pre = None

		while stack or root:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()

			if pre and pre.val > root.val:
				y = root
				# 暂时只找到一个点
				if not x:
					x = pre
				# 已经找到两个点 直接交换
				else:
					break

			pre = root
			root = root.right

		x.val, y.val = y.val, x.val



# Morris 中序遍历
# 时间复杂度 O(2N) = O(N)
# 空间复杂度 O(1)
'''
Morris 遍历算法整体步骤如下（假设当前遍历到的节点为 x）：

1. 如果 x 无左孩子, 则访问 x 的右孩子, 即 x = x.right
2. 如果 x 有左孩子, 则找到 x 左子树上最右的节点 (即左子树中序遍历的最后一个节点, x 在中序遍历中的前驱节点), 
	我们记为 predecessor, 根据 predecessor 的右孩子是否为空 进行如下操作:
	如果 predecessor 的右孩子为空则将其右孩子指向 x, 然后访问 x 的左孩子，即 x = x.left
	如果 predecessor 的右孩子不为空则说明此时其右孩子已经指向 x, 说明我们已经遍历完 x 的左子树, 我们将 predecessor 的右孩子置空
	然后访问 x 的右孩子, 即 x = x.right
3. 重复上述操作, 直至访问完整棵树
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def recoverTree(self, root):
		"""
		Do not return anything, modify root in-place instead.
		"""

		# 记录需要交换的两个点
		x, y = None, None
		pre, predecessor = None, None

		while root:
			if root.left:
				# predecessor 节点就是当前 root 节点向左走一步 然后一直向右走至无法走为止
				predecessor = root.left
				while predecessor.right and predecessor.right != root:
					predecessor = predecessor.right

				# 让 predecessor 指向 root 然后继续遍历左子树
				if not predecessor.right:
					predecessor.right = root
					root = root.left
				# 说明左子树已经访问完
				else:
					if pre and pre.val > root.val:
						y = root
						if not x:
							x = pre
					pre = root

					predecessor.right = None
					root = root.right

			# 如果无左子树 直接访问右子树
			else:
				if pre and pre.val > root.val:
					y = root
					if not x:
						x = pre
				pre = root
				root = root.right
				
		x.val, y.val = y.val, x.val
