# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 08:38:20
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 08:54:59


class Solution:
	def rotate(self, matrix):
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		# 先转置
		for i in range(len(matrix)):
			for j in range(i, len(matrix)):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		# 再每行倒序
		for i in range(len(matrix)):
			left, right = 0, len(matrix)-1
			while left <= right:
				matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
				left += 1
				right -= 1

				