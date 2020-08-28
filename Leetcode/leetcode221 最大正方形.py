# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 13:27:14
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 14:06:26


# 单调栈
class Solution:
	def maximalSquare(self, matrix):

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				matrix[i][j] = int(matrix[i][j])

		for i in range(1, len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] != 0:
					matrix[i][j] += matrix[i-1][j]

		for i in range(len(matrix)):
			matrix[i].append(0)

		def findmaxarea(arr):
			arr.append(0)
			stack = []
			maxSquare = 0
			for i in range(len(arr)):
				while stack and arr[stack[-1]] > arr[i]:
					top = stack.pop()
					if not stack:
						area = min(arr[top], i)
						maxSquare = max(maxSquare, area*area)
					else:
						area = min(arr[top], i-stack[-1]-1)
						maxSquare = max(maxSquare, area*area)
				stack.append(i)

			return maxSquare

		maxS = 0
		for row in matrix:
			maxS = max(maxS, findmaxarea(row))
		return maxS


# DP
'''
用 dp(i, j) 表示以 (i, j) 为右下角，且只包含 1 的正方形的边长最大值
如果该位置的值是 0，则 dp(i, j) = 0, 因为当前位置不可能在由 1 组成的正方形中
如果该位置的值是 1，则 dp(i, j) 的值由其上方、左方和左上方的三个相邻位置的 dp 值决定:
		dp(i, j) = min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1)) + 1
'''
class Solution:
	def maximalSquare(self, matrix):

		dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
		maxSide = 0

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == "1":
					if i == 0 or j == 0:
						dp[i][j] = 1
					else:
						dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

					maxSide = max(maxSide, dp[i][j])
		return maxSide * maxSide