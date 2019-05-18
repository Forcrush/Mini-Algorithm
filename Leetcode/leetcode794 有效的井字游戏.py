# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-14 21:25:50
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-14 22:08:59


'''
O的数量不能大于X的数量
X的数量超出O的数量不能大于1
不能同时存在O胜利和X胜利
如果O胜利，那么O的数量一定等于X的数量
如果X胜利，那么X的数量一定比O的数量多1s
'''
class Solution:
	def validTicTacToe(self, board):
		crossnum, circlenum = 0, 0
		for i in range(3):
			for j in range(3):
				if board[i][j] == 'X':
					crossnum += 1
				if board[i][j] == 'O':
					circlenum += 1

		if crossnum-circlenum not in [0, 1]:
			return False

		res = []
		for i in range(3):
			res.append(board[i][0] + board[i][1] + board[i][2])
		for j in range(3):
			res.append(board[0][j] + board[1][j] + board[2][j])
		res.append(board[0][0] + board[1][1] + board[2][2])
		res.append(board[0][2] + board[1][1] + board[2][0])

		if 'XXX' in res and crossnum-circlenum != 1:
			return False
		if 'OOO' in res and crossnum-circlenum != 0:
			return False

		return True