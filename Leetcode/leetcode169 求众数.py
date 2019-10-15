# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 12:10:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 14:50:01


# Boyer-Moore 投票算法
# 维护一个计数器 如果遇到一个我们目前的候选众数就将计数器加一 否则减一 
# 只要计数器等于 0 我们就将之前访问的数字全部忘记并把下一个数字当做候选的众数

# 时间复杂度 O(n)
# 空间复杂度 O(1)


class Solution:
	def majorityElement(self, nums):
		count = 0
		for i in nums:
			if count == 0:
				candidate = i
			count += (1 if candidate == i else -1)

		return candidate

		