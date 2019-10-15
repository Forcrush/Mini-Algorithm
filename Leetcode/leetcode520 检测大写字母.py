# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 09:39:03
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 09:48:02


# 不能通过判断两字符串ascii码差之和是否为 A-a 的整数倍来判断
# 因为可能存在字符错位攻击 所以只能逐个判断

class Solution:
	def detectCapitalUse(self, word):
		if len(word) <= 1:
			return True

		# 小写模式
		if ord(word[0]) >= 97:
			for i in range(1, len(word)):
				if 65 <= ord(word[i]) <= 90:
					return False
			return True

		if ord(word[0]) <= 90:
			# 全大写模式
			if ord(word[1]) <= 90:
				for i in range(2, len(word)):
					if 97 <= ord(word[i]) <= 122:
						return False
				return True

			# 首字母大写模式
			if ord(word[1]) >= 97:
				for i in range(2, len(word)):
					if 65 <= ord(word[i]) <= 90:
						return False
				return True