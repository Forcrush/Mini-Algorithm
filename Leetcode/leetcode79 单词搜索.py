# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-16 16:28:10
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-16 17:05:24


class Solution:
	def exist(self, board, word):

		start = []
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					start.append((i, j))

		if not start:
			return False
		if len(word) == 1:
			return True

		def DFS(point, word):
			stack = [(point, [point])]
			while stack:
				vertex, path = stack.pop()
				if len(path) == len(word):
					return True
				i, j = vertex
				for dx,dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
					if 0 <= i+dy < len(board) and 0 <= j+dx < len(board[0]):
						if board[i+dy][j+dx] == word[len(path)] and (i+dy, j+dx) not in path:
								newpath = path + [(i+dy, j+dx)]
								stack.append(((i+dy, j+dx), newpath))
			return False

		for point in start:
			if DFS(point, word):
				return True

		return False

