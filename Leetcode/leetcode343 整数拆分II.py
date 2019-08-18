# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-17 15:08:39
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-17 15:36:32


class Integer_Divide():
	def divide(self, num):
		res = []

		def recursion(array, rest):
			if rest == 0:
				res.append(array+[])
			for i in range(1, rest+1):
				if array == [] or (array != [] and i >= array[-1]):
					recursion(array+[i], rest-i)

		recursion([], num)

		return res

# print(Integer_Divide().divide(5))