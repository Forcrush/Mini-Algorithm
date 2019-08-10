# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-09 22:57:21
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-10 10:59:21


'''
思想类似桶排序算法。假设我们有容量为(t+1)的连续的桶可以覆盖掉所有的数字范围
那么对于差的绝对值最大为t的两个数，有两种情况：
（1）这两个数字在同一个桶中
（2）这两个数字在相邻桶中
'''
class Solution(object):
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		if t < 0:
			return False
		if len(nums) < 2:
			return False
		pool = {}
		for i in range(len(nums)):
			bucketid = nums[i] // (t + 1)
			if bucketid in pool:
				return True
			if bucketid - 1 in pool and abs(pool[bucketid-1] - nums[i]) <= t:
				return True
			if bucketid + 1 in pool and abs(pool[bucketid+1] - nums[i]) <= t:
				return True
			pool[bucketid] = nums[i]
			if i >= k:
				del pool[nums[i-k] // (t + 1)]
		return False
