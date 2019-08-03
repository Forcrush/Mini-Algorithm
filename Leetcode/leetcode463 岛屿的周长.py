# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 23:30:14
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 00:03:33


'''
因为不存在湖(内部空块), 因此只用找到边界块即可得到周长
'''
class Solution:
	def islandPerimeter(self, grid):
		row, col = len(grid), len(grid[0])
		perimeter = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j]:
					# 表示此块是在左边界或局部左边界上
					if j == 0 or grid[i][j-1] == 0:
						perimeter += 1
					# 表示此块是在上边界或局部上边界上
					if i == 0 or grid[i-1][j] == 0:
						perimeter += 1
		return perimeter * 2
