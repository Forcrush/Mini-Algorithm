# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-09 08:26:10
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-08-09 08:34:37


class Solution:
	def twoSum(self, numbers, target):
		if numbers == []:
			return []
		start = 0
		end = len(numbers) - 1
		if numbers[start] > target or numbers[end] < target:
			return []
		while start < end:
			if numbers[start] + numbers[end] == target:
				return [start+1, end+1]
			elif numbers[start] + numbers[end] < target:
				start += 1
			else:
				end -= 1
		return []