# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-14 14:55:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-14 15:39:21

'''
生命游戏规则
1 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡
2 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活
3 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡
4 如果死细胞周围正好有三个活细胞，则该位置死细胞复活
'''
class Solution:
	def gameOfLife(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		def legal_pos(x, y):
			return True if 0 <= x < len(board) and 0 <= y < len(board[0]) else False

		def get_round_grid(x, y):
			dx = [1, 0, -1]
			dy = [1, 0, -1]
			res = []
			for i in dx:
				for j in dy:
					if i != 0 or j != 0:
						res.append((x+i, y+j))
			return res

		for i in range(len(board)):
			for j in range(len(board[0])):
				# cell state from 0 -> 1 : 2
				# cell state from 1 -> 0 : 3
				live_neighbor = 0
				round_grid = get_round_grid(i, j)
				for ele in round_grid:
					if legal_pos(ele[0], ele[1]):
						# if 1 or 3 then previous state is live
						if board[ele[0]][ele[1]] in [1, 3]:
							live_neighbor += 1
				# rule1
				if live_neighbor < 2:
					board[i][j] = 3 if board[i][j] == 1 else 0

				# rule2.1
				if live_neighbor == 2:
					board[i][j] = 1 if board[i][j] == 1 else 0

				# rule2.2 rule 4
				if live_neighbor == 3:
					board[i][j] = 1 if board[i][j] == 1 else 2

				# rule 3
				if live_neighbor > 3:
					board[i][j] = 3 if board[i][j] == 1 else 0

		# update state 2 and 3 to 0 and 1
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 2:
					board[i][j] = 1
				if board[i][j] == 3:
					board[i][j] = 0

