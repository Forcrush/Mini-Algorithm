# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-06 23:12:16
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-07 11:16:27


class Solution:
	def pacificAtlantic(self, matrix):
		if sum(matrix, []) == []:
			return []
		row = len(matrix)
		col = len(matrix[0])

		def validposition(i, j):
			if i >= 0 and i <= row-1 and j >= 0 and j <= col-1:
				return True
			else:
				return False

		pacific = []
		atlantic = []
		for _ in range(row):
			pacific.append([False]*col)
			atlantic.append([False]*col)

		pacificstack = []
		atlanticstack = []

		for i in range(row):
			pacific[i][0] = True
			pacificstack.append((i, 0))
			atlantic[i][col-1] = True
			atlanticstack.append((i, col-1))
		for j in range(col):
			pacific[0][j] = True
			pacificstack.append((0, j))
			atlantic[row-1][j] = True
			atlanticstack.append((row-1, j))

		# 从太平洋海岸线向内陆搜寻
		while pacificstack != []:
			top = pacificstack.pop()
			for i in range(-1, 2, 2):
				if validposition(top[0]+i, top[1]):
					if matrix[top[0]+i][top[1]] >= matrix[top[0]][top[1]]:
						if pacific[top[0]+i][top[1]] == False:
							pacific[top[0]+i][top[1]] = True
							pacificstack.append((top[0]+i, top[1]))
				if validposition(top[0], top[1]+i):
					if matrix[top[0]][top[1]+i] >= matrix[top[0]][top[1]]:
						if pacific[top[0]][top[1]+i] == False:
							pacific[top[0]][top[1]+i] = True
							pacificstack.append((top[0], top[1]+i))

		# 从大西洋海岸线向内陆搜寻
		while atlanticstack != []:
			top = atlanticstack.pop()
			for i in range(-1, 2, 2):
				if validposition(top[0]+i, top[1]):
					if matrix[top[0]+i][top[1]] >= matrix[top[0]][top[1]]:
						if atlantic[top[0]+i][top[1]] == False:
							atlantic[top[0]+i][top[1]] = True
							atlanticstack.append((top[0]+i, top[1]))
				if validposition(top[0], top[1]+i):
					if matrix[top[0]][top[1]+i] >= matrix[top[0]][top[1]]:
						if atlantic[top[0]][top[1]+i] == False:
							atlantic[top[0]][top[1]+i] = True
							atlanticstack.append((top[0], top[1]+i))

		res = []
		for i in range(row):
			for j in range(col):
				if pacific[i][j] and atlantic[i][j]:
					res.append([i, j])
		return res

