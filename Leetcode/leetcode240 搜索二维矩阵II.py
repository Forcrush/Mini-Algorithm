# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-23 10:49:15
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-23 12:07:05


class Solution:
	def searchMatrix(self, matrix, target):

		def out_of_matrix(row, col):
			if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
				return False
			return True

		if len(matrix) < 1 or len(matrix[0]) < 1:
			return False

		# 从矩阵左下或右上开始
		row_st, col_st = 0, len(matrix[0])-1
		while True:
			if target == matrix[row_st][col_st]:
				return True
			elif target > matrix[row_st][col_st]:
				row_st += 1
			elif target < matrix[row_st][col_st]:
				col_st -= 1

			if out_of_matrix(row_st, col_st):
				return False
