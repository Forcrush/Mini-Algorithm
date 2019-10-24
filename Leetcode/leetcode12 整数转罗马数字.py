# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-23 08:42:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-23 08:45:31


class Solution:
	def intToRoman(self, num):
		values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

		index = 0
		res = ""
		while index < len(values):
			while num >= values[index]:
				res += romans[index]
				num -= values[index]
			index += 1

		return res
