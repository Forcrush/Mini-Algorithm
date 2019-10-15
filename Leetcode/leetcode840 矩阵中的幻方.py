# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 09:48:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 10:08:52


# 证明每行列及对角线之和必为15: 三行三列之和为全矩阵元素之和的两倍
# 证明3*3矩阵中心元素必为5: 包含中心的两对角线及两行列之和 = 15 * 4 = 1 + 2 + ... + 9 + 3*中心元素

class Solution:
	def numMagicSquaresInside(self, grid):
		if len(grid) < 3 or len(grid[0]) < 3:
			return 0

		def satisfy(i, j):
			if grid[i][j] + grid[i-1][j] + grid[i+1][j] != 15:
				return False
			if grid[i][j] + grid[i][j-1] + grid[i][j+1] != 15:
				return False
			if grid[i][j] + grid[i-1][j-1] + grid[i+1][j+1] != 15:
				return False
			if grid[i][j] + grid[i-1][j+1] + grid[i+1][j-1] != 15:
				return False
			if grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] != 15:
				return False
			if grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] != 15:
				return False
			if grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] != 15:
				return False
			if grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] != 15:
				return False
			x, y = [-1, 0, 1], [-1, 0, 1]
			point = []
			for dx in x:
				for dy in y:
					if grid[i+dx][j+dy] < 1 or grid[i+dx][j+dy] > 9:
						return False
					point.append(grid[i+dx][j+dy])
			if len(set(point)) != 9:
				return False
			return True

		res = 0
		# 判断以(i,j)为中心的3*3矩阵能否构成幻方
		for i in range(1, len(grid)-1):
			for j in range(1, len(grid[0])-1):
				if grid[i][j] != 5:
					continue
				if satisfy(i, j):
					res += 1
		return res
		