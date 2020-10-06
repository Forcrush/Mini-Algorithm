# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-19 14:56:27
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-19 15:15:50


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前缀和 递归
# 时间复杂度 O(N)
# 空间复杂度 O(N)
class Solution:
	def pathSum(self, root, sum):

		def recur_find(node, presum, target, cursum):
			if node == None:
				return 0

			cnt = 0
			cursum += node.val

			# 看看root到当前节点这条路上是否存在节点前缀和加target为currSum的路径
			# 当前节点->root节点反推，有且仅有一条路径，如果此前有和为currSum-target,而当前的和又为currSum,两者的差就肯定为target了
			# currSum-target相当于找路径的起点，起点的sum+target=currSum，当前点到起点的距离就是target
			cnt += presum.get(cursum-target, 0)

			# 更新路径上当前节点前缀和的个数
			presum[cursum] = presum.get(cursum, 0) + 1

			# 递归搜索下一层
			cnt += recur_find(node.left, presum, target, cursum)
			cnt += recur_find(node.right, presum, target, cursum)

			# 回到本层，恢复状态，去除当前节点的前缀和数量
			presum[cursum] -= 1

			return cnt

		# key是前缀和  value是大小为key的前缀和出现的次数
		presum = {}
		# 前缀和为0的一条路径
		presum[0] = 1

		return recur_find(root, presum, sum, 0)