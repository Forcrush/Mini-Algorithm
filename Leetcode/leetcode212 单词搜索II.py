# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-16 17:05:40
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-17 14:54:49


class Solution:
	def findWords(self, board, words):
		root = {}

		def insert(word):
			node = root
			for char in word:
				if char not in node:
					node[char] = {}
				node = node[char]
			# end of a word
			node['#'] = '#'

		for i in words:
			insert(i)

		res = []

		def search(i, j, node, path):
			if node.get(board[i][j], None) == None:
				return
			if node[board[i][j]].get('#', None) != None:
				w = ""
				for row,col in path:
					w += board[row][col]
				res.append(w)

			for dx,dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
				if 0 <= i+dy < len(board) and 0 <= j+dx < len(board[0]):
					if (i+dy, j+dx) not in path and node[board[i][j]].get(board[i+dy][j+dx], None) != None:
						newpath = path + [(i+dy, j+dx)]
						search(i+dy, j+dx, node[board[i][j]], newpath)

		for i in range(len(board)):
			for j in range(len(board[0])):
				search(i, j, root, [(i, j)])

		return list(set(res))

