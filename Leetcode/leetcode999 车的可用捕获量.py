# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 11:25:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 11:39:06


class Solution:
	def numRookCaptures(self, board):
		flag_r = False
		x, y = 0, 0
		for i in range(len(board)):
			if flag_r:
				break
			for j in range(len(board[0])):
				if board[i][j] == 'R':
					flag_r = True
					x, y = i, j
					break
		if not flag_r:
			return 0
		res = 0

		for i in range(x, len(board[0])):
			if board[i][y] == 'p':
				res += 1
				break
			if board[i][y] == 'B':
				break
		for i in range(x, 0, -1):
			if board[i][y] == 'p':
				res += 1
				
				break
			if board[i][y] == 'B':
				break
		for j in range(y, len(board)):
			if board[x][j] == 'p':
				res += 1
				break
			if board[x][j] == 'B':
				break
		for j in range(y, 0, -1):
			if board[x][j] == 'p':
				res += 1
				break
			if board[x][j] == 'B':
				break
		return res
