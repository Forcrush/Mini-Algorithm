# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-27 14:41:50
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-27 14:50:10


'''
考虑所有数字的同一个bit位，统计在这个bit位上出现的1的次数count，
那么这个bit位在总的汉明距离中就贡献了count*(n-count)，n是数组中元素的个数
时间复杂度 O(n)
'''
class Solution:
	def totalHammingDistance(self, nums):
		toldis = 0
		for _ in range(32):
			count = 0
			for i in range(len(nums)):
				if nums[i] & 1:
					count += 1
				nums[i] >>= 1
			toldis += count * (len(nums) - count)

		return toldis

