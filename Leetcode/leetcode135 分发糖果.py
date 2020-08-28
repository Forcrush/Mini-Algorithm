# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 17:47:39
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 17:52:14


class Solution:
	def candy(self, ratings):

		candies = [1] * len(ratings)

		# 先从左遍历
		for i in range(1, len(ratings)):
			if ratings[i] > ratings[i-1]:
				candies[i] = candies[i-1] + 1

		# 从右遍历
		for j in range(len(ratings)-2, -1, -1):
			if ratings[j] > ratings[j+1]:
				candies[j] = max(candies[j], candies[j+1]+1)

		return sum(candies)