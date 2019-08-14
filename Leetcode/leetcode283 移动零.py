# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-12 15:30:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-14 22:45:24


class Solution:
	def moveZeroes(self, nums):
		zero = -1
		for i in range(len(nums)):
			if nums[i] != 0 and zero >= 0:
				nums[i], nums[zero] = nums[zero], nums[i]
				# +1后的位置必为0
				zero += 1
			elif nums[i] == 0 and zero == -1:
				zero = i

		return nums

