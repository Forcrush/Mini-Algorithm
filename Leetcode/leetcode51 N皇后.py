# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 13:27:15
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-07 21:40:54


# 递归法
class Solution:
	def solveNQueens(self, n):
		if n == 1:
			return [['Q']]
		if n == 0 or n == 2 or n==3:
			return []

		board = [0] * n
		res = []

		# check if there is a conflict
		def check(x, y):
			for i in range(x):
				if board[i] == y or abs(i - x) == abs(board[i] - y):
					return 0
			return 1

		# begin to set the chess from 1st row
		def place(row):
			if row > n-1:
				# res.append(board) will cause an error !!!
				res.append(board + [])
			else:
				for j in range(1, n+1):
					if check(row, j):
						board[row] = j
						place(row+1)

		def transform(num):
			return '.' * (num - 1 ) + 'Q' + '.' * (n - num)

		place(0)

		if res == []:
			return []
		else:
			for i in range(len(res)):
				for j in range(n):
					res[i][j] = transform(res[i][j])

		return res
