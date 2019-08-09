# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 22:31:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-09 22:51:24


'''
在散列表中搜索当前元素 如果找到了就返回 true
在散列表中插入当前元素
如果当前散列表的大小超过了k 删除散列表中最旧的元素
'''
class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		pool = set()
		for i in range(len(nums)):
			if nums[i] in pool:
				return True
			else:
				pool.add(nums[i])
			if len(pool) > k + 1:
				pool.remove(nums[i-k])
		return False

		