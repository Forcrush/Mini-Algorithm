# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-06 01:01:50
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-06 12:43:22


'''
Inverse DP
dp[i][j] means the minimum life-value to get to (i, j), 
it depends on its later path but not former path
'''
class Solution:
	def calculateMinimumHP(self, dungeon):
		row = len(dungeon)
		col = len(dungeon[0])

		dp = []
		for _ in range(row):
			dp.append([0]*col)
		if dungeon[row-1][col-1] > 0:
			dp[row-1][col-1] = 1
		else:
			dp[row-1][col-1] = abs(dungeon[row-1][col-1]) + 1

		if row > 1:
			for i in range(row-2, -1, -1):
				if dungeon[i][col-1] - dp[i+1][col-1] >= 0:
					dp[i][col-1] = 1
				else:
					dp[i][col-1] = abs(dungeon[i][col-1] - dp[i+1][col-1])

		if col > 1:
			for j in range(col-2, -1, -1):
				if dungeon[row-1][j] - dp[row-1][j+1] >= 0:
					dp[row-1][j] = 1
				else:
					dp[row-1][j] = abs(dungeon[row-1][j] - dp[row-1][j+1])

		if row > 1 and col > 1:
			for i in range(row-2, -1, -1):
				for j in range(col-2, -1, -1):
					if dp[i+1][j] < dp[i][j+1]:
						if dungeon[i][j] - dp[i+1][j] >= 0:
							dp[i][j] = 1
						else:
							dp[i][j] = abs(dungeon[i][j] - dp[i+1][j])
					else:
						if dungeon[i][j] - dp[i][j+1] >= 0:
							dp[i][j] = 1
						else:
							dp[i][j] = abs(dungeon[i][j] - dp[i][j+1])

		return dp[0][0]

