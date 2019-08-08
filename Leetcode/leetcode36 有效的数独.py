# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-06 22:14:27
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-06 22:41:07


class Solution:
	def isValidSudoku(self, board):
		row = [{} for i in range(9)]
		col = [{} for i in range(9)]
		subbox = [{} for i in range(9)]
		for i in range(9):
			for j in range(9):
				if board[i][j] != '.':
					num = int(board[i][j])
					boxindex = (i // 3) * 3 + j // 3
					row[i][num] = row[i].get(num, 0) + 1
					col[j][num] = col[j].get(num, 0) + 1
					subbox[boxindex][num] = subbox[boxindex].get(num, 0) + 1

					if row[i][num] > 1 or col[j][num] > 1 or subbox[boxindex][num] > 1:
						return False
		return True

		