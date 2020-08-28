# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 14:24:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 14:46:37


class Solution:
	def findMinHeightTrees(self, n, edges):

		graph, neighbor = {}, {}
		for i in range(n):
			graph[i] = 0
			neighbor[i] = []

		for n1, n2 in edges:
			graph[n1] += 1
			graph[n2] += 1
			neighbor[n1].append(n2)
			neighbor[n2].append(n1)

		delete = []
		while True:
			if n - len(delete) in [1, 2]:
				break

			tmp = []
			for k,v in graph.items():
				if graph[k] == 1:
					graph[k] -= 1
					tmp.append(k)
					delete.append(k)
			for k in tmp:
				for nb in neighbor[k]:
					graph[nb] -= 1
		res = list(set([i for i in range(n)]) - set(delete))

		return res

		