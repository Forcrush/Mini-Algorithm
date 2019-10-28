# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-25 12:47:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-25 13:37:59


class Solution:
	def threeSumClosest(self, nums, target):
		if len(nums) <= 3:
			return sum(nums)
		nums.sort()
		res = float("+inf")
		for i in range(len(nums)-1):
			start, end = i+1, len(nums)-1
			while start < end:
				curSum = nums[i] + nums[start] + nums[end]
				if abs(curSum-target) < abs(res-target):
					res = curSum
				if curSum > target:
					end -= 1
				elif curSum < target:
					start += 1
				else:
					return curSum

		return res

