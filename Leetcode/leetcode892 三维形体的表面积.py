# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-24 20:12:39
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-24 20:55:23


class Solution:
	def surfaceArea(self, grid):
		surface = 0
		n = len(grid)

		# 上下表面积
		takeplace = 0
		for i in range(n):
			for j in range(n):
				if grid[i][j] > 0:
					takeplace += 1
		surface += takeplace * 2

		# 最外侧四面面积
		for i in range(n):
			surface += grid[0][i]
			surface += grid[n-1][i]
			surface += grid[i][0]
			surface += grid[i][n-1]

		# 内侧面积
		def ingrid(xpos, ypos, n):
			if 0 <= xpos <= n-1 and 0 <= ypos <= n-1:
				return True
			return False

		xdir = [1, -1, 0, 0]
		ydir = [0, 0, 1, -1]
		for i in range(n):
			for j in range(n):
				for k in range(4):
					if ingrid(i+xdir[k], j+ydir[k], n):
						adjacent = grid[i+xdir[k]][j+ydir[k]]
						surface += max(grid[i][j] - adjacent, 0)

		return surface

