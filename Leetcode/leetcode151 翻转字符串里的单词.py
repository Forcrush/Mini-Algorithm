# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-03-09 19:14:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-03-09 19:56:02


# 因为Python不能直接修改字符串而C语言中字符串其实是Char数组
# 因此以下的思想方法对C语言来说可以只用 O(1) 的额外空间复杂度完成
class Solution:
	def reverseWords(self, s):
		if s == "": return ""
		# 为了方便处理 首位加上空格
		s = " " + s + " "
		s = list(s)

		# 原地反转区间
		def reverseInterval(start, end):
			p1, p2 = start, end
			while p1 <= p2:
				s[p1], s[p2] = s[p2], s[p1]
				p1 += 1
				p2 -= 1
		
		# 先反转整个字符串
		reverseInterval(0, len(s)-1)
		
		# 再反转每个单词 flag表示是否遇到一个单词的开头
		flag = False
		p1, p2 = 0, 0
		for i in range(len(s)):
			if s[i] != " " and not flag:
				p1 = i
				flag = True
			if s[i] == " " and flag and s[i-1] != " ":
				p2 = i-1
				flag = False
				reverseInterval(p1, p2)

		# 去除多余空格
		# 先去除开头的空格
		pos = 0
		while pos < len(s):
			if s[pos] == " ":
				s.pop(pos)
			else:
				break
		# 去除中间的空格
		while pos < len(s)-1:
			if s[pos] == " " and s[pos+1] == " ":
				s.pop(pos)
			else:
				pos += 1
		# 因为pos只检测到len(s)-2位置 需要再判断最后一位是否为空格
		if not s: return ""
		if s[-1] == " ":
			s.pop()

		return "".join(s)

