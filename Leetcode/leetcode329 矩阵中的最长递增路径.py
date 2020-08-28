# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-17 23:23:26
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-18 00:02:44


class Solution:
	def longestIncreasingPath(self, matrix):
		dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

		def get_around(i, j):
			res = []
			direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
			for x,y in direction:
				if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
					res.append((i+x, j+y))
			return res

		def find_path(x, y):
			# alreay been searched and stored in dp[][]
			if dp[x][y]:
				return dp[x][y]
			candidate = []
			for m,n in get_around(x, y):
				if matrix[m][n] > matrix[x][y]:
					candidate.append(find_path(m, n))
			# this point is peak point, also end of a path
			if not candidate:
				dp[x][y] = 1
				return dp[x][y]
			else:
				dp[x][y] = 1 + max(candidate)
				return dp[x][y]

		
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				dp[i][j] = find_path(i, j)

		res = -1
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				res = max(res, dp[i][j])
		
		return res

