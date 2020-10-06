# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-18 15:04:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-18 15:09:46


# 约瑟夫环变体
# f(2k)/f(2k+1) is the old || f(k) is the new
# f(2k) = 2(k+1−f(k))
# f(2k+1) = 2(k+1−f(k))
# ===> f(n) = 2 * (⌊n/2⌋ + 1 - f(⌊n/2⌋))
class Solution:
	def lastRemaining(self, n):
		return 1 if n == 1 else 2 * (n // 2 + 1 - self.lastRemaining(n//2))