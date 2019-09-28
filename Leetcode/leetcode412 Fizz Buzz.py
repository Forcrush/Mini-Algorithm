# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 09:11:06
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 13:55:01


class Solution:
	def fizzBuzz(self, n):
		res = []
		for i in range(1, n+1):
			if i%3 == 0 and i%5 == 0:
				res.append('FizzBuzz')
			elif i%3 == 0:
				res.append('Fizz')
			elif i%5 == 0:
				res.append('Buzz')
			else:
				res.append(str(i))
		return res