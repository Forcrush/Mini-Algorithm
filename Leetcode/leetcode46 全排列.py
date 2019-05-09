# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 11:33:29
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-09 12:14:09


'''
递归法
将数组每个数与第一个数交换 同样处理去除掉第一个数后的数组：
[1, 3, 5]
--> [1, 3, 5] --> [3, 5] --> [5] --> 1 3 5
              --> [5, 3] --> [3] --> 1 5 3

--> [3, 1, 5] --> [1, 5] --> [5] --> 3 1 5
              --> [5, 1] --> [1] --> 3 5 1

--> [5, 3, 1] --> [3, 1] --> [1] --> 5 3 1
              --> [1, 3] --> [3] --> 5 1 3

'''
class Solution:
	def permute(self, nums):
		res = []
		if nums == []:
			return res
		def search(array, start, end):
			if start == end:
				res.append(array+[])
			else:
				for i in range(start, end+1):
					array[start], array[i] = array[i], array[start]
					search(array, start+1, end)
					# restore the array before exchange
					array[start], array[i] = array[i], array[start]

		search(nums, 0, len(nums)-1)
		return res