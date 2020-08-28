# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 12:21:20
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 13:04:45


# Manacher (但找的是在原串中开头的最长回文串)
class Solution:
	def shortestPalindrome(self, s):
		news = "#"
		for i in s:
			news += i
			news += "#"
		radius = [0] * len(news)
		center, finalcenter, finalradius = 0, 0, 0
		rightboundary = 0

		for i in range(1, len(news)):
			if i < rightboundary:
				j = 2 * center - i
				if radius[j] <= rightboundary - i:
					radius[i] = radius[j]
				else:
					radius[i] = rightboundary - i + 1
			else:
				radius[i] = 1
			while(i - radius[i] >= 0 and i + radius[i] < len(news) and news[i - radius[i]] == news[i + radius[i]]):
				radius[i] += 1
			if i + radius[i] > rightboundary:
				rightboundary = i + radius[i] - 1
				center = i
			if radius[i] > finalradius:
				finalradius = radius[i]
				finalcenter = i

		maxpos = 0
		for i in range(len(news)):
			# 找到的最长回文串需要在原串串首
			if i - radius[i] + 1 == 0:
				maxpos = max(maxpos, i)

		cnt = 0
		# 统计找到的最长回文串中有多少字母
		for j in news[maxpos-radius[maxpos]+1:maxpos+radius[maxpos]]:
			if j != "#":
				cnt += 1

		return s[cnt:][::-1] + s


# KMP
'''
核心思想还是找到从字符串开头的最长回文串

反转原始字符串 s 为 rev 拼接成新串 new = s + rev
找到新串的最长前缀 即有 s[:i] == rev[n-i:]
因为 res = s[::-1], 此时s[:i]必为回文串

结果就是 res[:i] + s
'''
class Solution:
	def shortestPalindrome(self, s):

		# '#'很有必要 避免混淆 s 和 rev, 比如 s = "aaaa" 的情况
		new = s + "#" + s[::-1]

		# KMP的next数组
		# next[i] 表示长度为 i+1 的数组最长前缀长度为 next[i]+1
		next = [-1] * len(new)
		k = -1
		for i in range(1, len(new)):
			while k > -1 and new[k+1] != new[i]:
				k = next[k]
			if new[k+1] == new[i]:
				k += 1
			next[i] = k

		length = next[len(new)-1] + 1

		return s[::-1][:len(s)-length] + s