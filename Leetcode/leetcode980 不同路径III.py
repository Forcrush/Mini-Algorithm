# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-07 19:13:49
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-07 20:04:01


class Solution:
	def uniquePathsIII(self, grid):
		if sum(grid, []) == []:
			return 0
		row = len(grid)
		col = len(grid[0])

		# number of 1
		startnum = 0
		# number of 2
		endnum = 0
		# number of 0
		zeronum = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 0:
					zeronum += 1
				elif grid[i][j] == 1:
					startnum += 1
					start = (i, j)
				elif grid[i][j] == 2:
					endnum += 1
					end = (i, j)
		if startnum != 1 or endnum != 1:
			return 0

		def validvertex(i, j):
			if i >= 0 and i <= row-1 and j >= 0 and j <= col-1:
				return True
			else:
				return False

		totalpath = []
		stack = [(start, [(start[0], start[1])])]
		while stack != []:
			vertex, path = stack.pop()
			direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
			for i, j in direction:
				# 合法点
				if validvertex(vertex[0]+i, vertex[1]+j):
					# 未路过此点
					if (vertex[0]+i, vertex[1]+j) not in path:
						if grid[vertex[0]+i][vertex[1]+j] == 0:
							stack.append(((vertex[0]+i, vertex[1]+j), path + [(vertex[0]+i, vertex[1]+j)]))
						elif grid[vertex[0]+i][vertex[1]+j] == 2:
							# path包含了初始点
							if len(path) == zeronum+1:
								totalpath.append(path + [(vertex[0]+i, vertex[1]+j)])

		if totalpath == []:
			return 0
		else:
			return len(totalpath)

