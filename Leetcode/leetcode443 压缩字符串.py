# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 13:16:04
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 14:36:07


class Solution:
	def compress(self, chars):
		if len(chars) == 0 or len(chars) == 1:
			return len(chars)
		start = 0
		newarray = 0
		for i in range(len(chars)-1):
			if i == len(chars)-2:
				if chars[i] == chars[i+1]:
					chars[newarray] = chars[i]
					newarray += 1
					for j in str(i-start+2):
						chars[newarray] = j
						newarray += 1
					break
				else:
					if i-start+1 == 1:
						chars[newarray] = chars[i]
						newarray += 1
					else:
						chars[newarray] = chars[i]
						newarray += 1
						for j in str(i-start+1):
							chars[newarray] = j
							newarray += 1
					chars[newarray] = chars[-1]
					newarray += 1
					break

			if chars[i] == chars[i+1]:
				continue
			else:
				if i-start+1 == 1:
					chars[newarray] = chars[i]
					newarray += 1
					start = i+1
				else:
					chars[newarray] = chars[i]
					newarray += 1
					for j in str(i-start+1):
						chars[newarray] = j
						newarray += 1
					start = i+1
		for k in range(len(chars)-1, newarray-1, -1):
			chars.pop()

		return len(chars)

