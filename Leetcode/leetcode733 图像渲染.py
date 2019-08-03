# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 00:03:47
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 00:47:07


class Solution:
	def floodFill(self, imag, sr, sc, newColor):
		def isvalid(x, y):
			if 0 <= x <= len(imag)-1 and 0 <= y <= len(imag[0])-1:
				return True
			else:
				return False
		xdir = [1, 0, -1 ,0]
		ydir = [0, -1, 0, 1]
		stack = [(sr, sc)]
		render = []
		while stack:
			point = stack.pop()
			render.append(point)
			for i in range(4):
				if isvalid(point[0]+xdir[i], point[1]+ydir[i]):
					if imag[point[0]+xdir[i]][point[1]+ydir[i]] == imag[point[0]][point[1]]:
						if (point[0]+xdir[i], point[1]+ydir[i]) not in render:
							stack.append((point[0]+xdir[i], point[1]+ydir[i]))
							render.append((point[0]+xdir[i], point[1]+ydir[i]))
		for item in render:
			imag[item[0]][item[1]] = newColor

		return imag

		