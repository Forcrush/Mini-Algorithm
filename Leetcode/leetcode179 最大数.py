# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-18 22:38:11
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-18 23:00:47


class Solution:
	def largestNumber(self, nums):

		import functools

		# 自定义两字符串大小比较关系
		def chy(a, b):
			if a + b > b + a:
				# return -1 说明无需交换
				return -1
			else:
				# return 1 说明需交换
				return 1

		new_list = sorted(list(map(str, nums)), key=functools.cmp_to_key(chy))

		return '0' if new_list[0] == '0' else ''.join(new_list)


'''
a=[3,30,34,5,9]
print(Solution().largestNumber(a))
'''