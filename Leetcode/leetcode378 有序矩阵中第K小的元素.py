# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-26 14:59:04
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-26 17:07:11


class Solution:
	def kthSmallest(self, matrix, k):
		
		left, right = matrix[0][0], matrix[-1][-1]


		# 计算小于等于mid的元素个数
		def cntSmaller(matrix, mid):
			x, y = len(matrix)-1, 0
			start = (x, y)
			cnt = 0
			while x >= 0 and y < len(matrix[0]):
				if matrix[x][y] <= mid:
					cnt += x+1
					y += 1
				else:
					x -= 1
			return cnt

		while left < right:
			mid = right + (left - right) // 2
			count = cntSmaller(matrix, mid)
			# 保持第k小的元素一直在 [left, right] 内
			# 当 left == right 时 即为所求元素
			if count < k:
				left = mid + 1
			else:
				right = mid
		
		return left

