# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-08 14:43:43
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-08 19:22:43


class Solution:
	def solveSudoku(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		row = [[False for i in range(9)] for i in range(9)]
		col = [[False for i in range(9)] for i in range(9)]
		box = [[False for i in range(9)] for i in range(9)]

		for i in range(9):
			for j in range(9):
				if board[i][j] != '.':
					num = int(board[i][j])
					row[i][num-1] = True
					col[j][num-1] = True
					box[(i // 3) * 3 + j // 3][num-1] = True

		self.solved = False

		def nextpos(x, y):
			if y < 8:
				return x, y + 1
			else:
				return x + 1, 0

		def solve(i, j):
			if i > 8:
				self.solved = True
				return
			nexti, nextj = nextpos(i, j)
			if board[i][j] != '.':
				solve(nexti, nextj)
			else:
				for k in range(9):
					if not row[i][k] and not col[j][k] and not box[(i // 3) * 3 + j // 3][k]:
						row[i][k] = True
						col[j][k] = True
						box[(i // 3) * 3 + j // 3][k] = True
						board[i][j] = str(k+1)
						solve(nexti, nextj)

						if not self.solved:
							row[i][k] = False
							col[j][k] = False
							box[(i // 3) * 3 + j // 3][k] = False
							board[i][j] = '.'


		solve(0, 0)

# sample = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]