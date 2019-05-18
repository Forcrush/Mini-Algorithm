# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-14 18:48:36
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-14 21:19:34


class Solution(object):
	def canPartitionKSubsets(self, nums, k):
		if k == 1:
			return True
		if len(nums) < k:
			return False
		total = sum(nums)
		if total % k:
			return False
			
		target = total / k

		# 记录使用过的点
		visited = [0] * len(nums)

		# start为搜索起点 cursum为目前子集和 cnt为目前使用过的数字数量
		def dfs(k, start, cursum, cnt):
			if k == 1:
				return True
			if cursum == target and cnt > 0:
				return dfs(k - 1, 0, 0, 0)
			for i in range(start, len(nums)):
				if not visited[i] and cursum + nums[i] <= target:
					visited[i] = 1
					if dfs(k, i + 1, cursum + nums[i], cnt + 1):
						return True
					visited[i] = 0
			return False

		return dfs(k, 0, 0, 0)

