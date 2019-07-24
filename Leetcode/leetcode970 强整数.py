# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-24 18:21:30
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-24 19:22:02


'''
如果 x^i > bound, 那么 x^i + y^j 也不可能小于等于 bound 对于 y^j 也是同样的道理
因此只需要对于所有的 0 < i, j < log_x(bound) < 20 遍历即可 (根据题意指数最大值为log_2(10^6))

时间复杂度：O(log(bound)^2)
空间复杂度：O(log(bound)^2)
'''
class Solution:
	def powerfulIntegers(self, x, y, bound):
		# 令 i,j 的遍历上限为 m,n
		if x == 1:
			m = 1
		else:
			# m = math.log(bound, x)
			m = 20
		if y == 1:
			n = 1
		else:
			# n = math.log(bound, y)
			n = 20
		res = set()
		for i in range(m):
			for j in range(n):
				if x ** i + y ** j <= bound:
					res.add(x ** i + y ** j)
				else:
					break
		return list(res)