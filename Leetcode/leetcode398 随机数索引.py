# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-17 11:11:56
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-17 11:35:50


# 蓄水池抽样
class Solution:

	def __init__(self, nums):
		self.nums = nums

	def pick(self, target):
		import random

		# 因为是从N个数抽一个出来 pool可以用单变量来代替数组
		pool = None
		n = 0
		for i in range(len(self.nums)):
			if self.nums[i] == target:
				n += 1
				if pool == None:
					pool = i
				elif random.randint(0, n-1) == 0:
					pool = i
		return pool

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)