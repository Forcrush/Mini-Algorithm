# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-30 22:22:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-30 22:31:29


# 时间复杂度 O(N)
# 空间复杂度 O(1)--不算输出空间
class Solution:
	def productExceptSelf(self, nums):

		res = [1] * len(nums)

		# 计算左侧前缀之积
		for i in range(1, len(res)):
			res[i] = res[i-1] * nums[i-1]

		right_sum = 1
		print(res)
		# 计算右侧前缀之积同时计算两边之积
		for j in range(len(res)-2, -1, -1):
			right_sum *= nums[j+1]
			res[j] *= right_sum

		return res

