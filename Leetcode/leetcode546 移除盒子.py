# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-10-05 20:07:30
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-10-05 20:26:37


# Details: https://leetcode-cn.com/problems/remove-boxes/solution/yi-chu-he-zi-by-leetcode-solution/
class Solution:
	def removeBoxes(self, boxes):

		def cal_points(boxes, l, r, k):
			if l > r: return 0
			if dp[l][r][k]: return dp[l][r][k]

			# 优化步 与right位连续的相同元素可直接消掉
			while r > l and boxes[r] == boxes[r-1]:
				k += 1
				r -= 1

			dp[l][r][k] = cal_points(boxes, l, r-1, 0) + (k+1)**2
			for i in range(l, r):
				if boxes[i] == boxes[r]:
					dp[l][r][k] = max(dp[l][r][k], cal_points(boxes, l, i, k+1) + cal_points(boxes, i+1, r-1, 0))

			return dp[l][r][k]

		dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]

		return cal_points(boxes, 0, len(boxes)-1, 0)


# 记忆化搜索 优化
class Solution2:
	def removeBoxes(self, boxes):

		def cal_points(boxes, l, r, k):
			if l > r: return 0

			if (l, r, k) in memo: return memo[(l, r, k)]

			# 优化步 与right位连续的相同元素可直接消掉
			while r > l and boxes[r] == boxes[r-1]:
				k += 1
				r -= 1

			res = cal_points(boxes, l, r-1, 0) + (k+1)**2
			for i in range(l, r):
				if boxes[i] == boxes[r]:
					res = max(res, cal_points(boxes, l, i, k+1) + cal_points(boxes, i+1, r-1, 0))

			memo[(l, r, k)] = res
			return res

		memo = {}

		return cal_points(boxes, 0, len(boxes)-1, 0)
