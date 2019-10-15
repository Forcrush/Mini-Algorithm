# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-12 15:15:11
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-12 15:20:51


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
	def rand10(self):
		while True:
			flag1 = rand7()
			if flag1 == 4:
				continue
			# 1,2,3 -> 1,2,3,4,5
			elif flag1 < 4:
				while True:
					flag2 = rand7()
					if flag2 < 6:
						return flag2
					else:
						continue

			# 5,6,7 -> 6,7,8,9,10
			elif flag1 > 4:
				while True:
					flag2 = rand7()
					if flag2 < 6:
						return flag2 + 5
					else:
						continue