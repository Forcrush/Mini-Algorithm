# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 12:40:54
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 12:55:24


class Solution():
	def minSubArrayLen(self, s, nums):
		left, right, total = 0, 0, 0
		length = len(nums) + 1
		while right < len(nums):
			total += nums[right]
			right += 1
			while total >= s:
				if right - left < length:
					length = right - left
				total -= nums[left]
				left += 1

		if length == len(nums) + 1:
			return 0
		return length

