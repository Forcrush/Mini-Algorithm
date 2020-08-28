# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-04 22:27:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-04 22:59:23


class Solution:
	def removeDuplicates(self, nums):

		if len(nums) <= 2: return len(nums)

		cur = 1
		candidate = nums[0]
		cnt = 1
		for i in range(1, len(nums)):
			if nums[i] != candidate:
				candidate = nums[i]
				nums[cur], nums[i] = nums[i], nums[cur]				
				cnt = 1
				cur += 1
			else:
				if cnt < 2:
					nums[cur], nums[i] = nums[i], nums[cur]
					print(i,nums)
					cnt += 1
					cur += 1
				else:
					continue

		return cur

