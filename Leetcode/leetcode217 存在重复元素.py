# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 22:29:01
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 22:31:04


class Solution(object):
	def containsDuplicate(self, nums):
		return not len(nums) == len(set(nums))