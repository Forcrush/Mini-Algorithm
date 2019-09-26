# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-24 11:39:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-24 12:20:28


class NumArray:

	def __init__(self, nums):
		self.nums = nums
		self.sum_nums = self.sumArray(nums)

	def sumArray(self, nums):
		sum_nums = [nums[i] for i in range(0, len(nums))]
		for i in range(1, len(sum_nums)):
			sum_nums[i] += sum_nums[i-1]
		return sum_nums

	def sumRange(self, i, j):
		return self.sum_nums[j] - self.sum_nums[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

