# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-13 14:30:22
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-13 17:33:19


# DFS (BFS同理)
class Solution:
	def numIslands(self, grid):

		if not grid: return 0

		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					stack = [(i, j)]
					count += 1
					grid[i][j] = '0'
					while stack:
						row, col = stack.pop()
						for x,y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
							if 0 <= row+y < len(grid) and 0 <= col+x < len(grid[0]) and grid[row+y][col+x] == '1':
								grid[row+y][col+x] = '0'
								stack.append((row+y, col+x))
		return count


# Find-Union 并查集
class Solution2:
	def numIslands(self, grid):

		if not grid: return 0

		def find(x):
			if x != parent[x]:
				parent[x] = find(parent[x])
			return parent[x]

		def union(a, b):
			aroot, broot = find(a), find(b)
			if aroot == broot:
				return

			if rank[aroot] > rank[broot]:
				parent[broot] = aroot
			elif rank[aroot] < rank[broot]:
				parent[aroot] = broot
			else:
				parent[aroot] = broot
				rank[broot] += 1

		def getIndex(i, j):
			return i * len(grid[0]) + j

		# rank 记录一个并查集的规模
		rank = [1 for _ in range(len(grid) * len(grid[0]))]
		# parent 记录父节点
		parent = [0 for _ in range(len(grid) * len(grid[0]))]
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				index = getIndex(i, j)
				parent[index] = index

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					# 可以只考虑右和下两个方向
					for dx,dy in [(1, 0), (0, 1)]:
						if 0 <= i+dy < len(grid) and 0 <= j+dx < len(grid[0]) and grid[i+dy][j+dx] == '1':
							index1, index2 = getIndex(i, j), getIndex(i+dy, j+dx)
							if find(index1) != find(index2):
								union(index1, index2)

		res = []
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					res.append(find(getIndex(i, j)))
		return len(list(set(res)))

