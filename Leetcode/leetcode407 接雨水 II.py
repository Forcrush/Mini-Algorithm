# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-19 13:45:37
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-19 13:58:47


class Solution:
	def trapRainWater(self, heightMap):
		import heapq as hq
		
		res = 0
		arr = []
		visited = [[False for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]

		# 将最外围一圈元素入堆
		for i in range(len(heightMap)):
			for j in range(len(heightMap[0])):
				if i == 0 or j == 0 or i == len(heightMap)-1 or j == len(heightMap[0])-1:
					hq.heappush(arr, (heightMap[i][j], i, j))
					visited[i][j] = True

		while arr:
			h, x, y = hq.heappop(arr)
			# 寻找最小元素的四个方向
			for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
				if 0 <= x+dx < len(heightMap) and 0 <= y+dy < len(heightMap[0]) and not visited[x+dx][y+dy]:
					# 某一个方向比当前位置矮 可以灌水
					if heightMap[x+dx][y+dy] < h:
						res += h - heightMap[x+dx][y+dy]

					# 灌水后以灌水后高度入堆
					hq.heappush(arr, (max(h, heightMap[x+dx][y+dy]), x+dx, y+dy))
					visited[x+dx][y+dy] = True

		return res