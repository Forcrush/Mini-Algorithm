# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-24 20:58:58
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-24 22:01:33


'''
http://keithschwarz.com/interesting/code/?dir=find-duplicate
'''
class Solution:
	def findDuplicate(self, nums):
		slow = 0
		fast = 0
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break

		finder = 0
		while True:
			finder = nums[finder]
			slow = nums[slow]
			if finder == slow:
				return finder