# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-26 21:19:10
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-26 21:53:02


# 二分 思路同 leetcode378
class Solution:
	def smallestDistancePair(self, nums, k):
		nums.sort()
		left, right = nums[0], nums[-1]

		# 计算距离小于等于mid的距离对数
		def cntSmaller(nums, mid):
			cnt, j = 0, 0
			for i in range(1, len(nums)):
				while nums[i] - nums[j] > mid:
					j += 1
				cnt += i-j
			return cnt

		# 第 k 小的距离一定在 [left, right] 内
		while left < right:
			mid = right + ((left - right) >> 1)
			cnt = cntSmaller(nums, mid)
			if cnt < k:
				left = mid + 1
			else:
				right = mid

		return left

