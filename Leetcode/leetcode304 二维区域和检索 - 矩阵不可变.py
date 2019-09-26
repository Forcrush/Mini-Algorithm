# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-25 17:04:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-25 17:53:19


class NumMatrix:

	def __init__(self, matrix):
		self.sum_matrix = self.init_matrix(matrix)

	def init_matrix(self, matrix):
		if matrix == [] or matrix == [[]] or matrix == [[[]]]:
			return None
		# 最外一层嵌入0 方便计算
		sum_matrix = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]

		for i in range(0, len(matrix)):
			for j in range(0, len(matrix[0])):
				sum_matrix[i+1][j+1] = sum_matrix[i][j+1] + sum_matrix[i+1][j] + matrix[i][j] - sum_matrix[i][j]

		return sum_matrix		

	def sumRegion(self, row1, col1, row2, col2):
		if self.sum_matrix:
			return self.sum_matrix[row2+1][col2+1] - self.sum_matrix[row2+1][col1] - self.sum_matrix[row1][col2+1] + self.sum_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)