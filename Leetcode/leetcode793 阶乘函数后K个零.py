# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-23 12:07:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-23 13:22:51


'''
* 阶乘
*      	 x 		K/f(x)
* 1个5 = 5		1
* 2个5 = 25		6   实际相当于 5个1个5 然后再加25自身是两个5 所以得到的是 5+1 = 6
* 3个5 = 125		31  相当于5个25 然后加自身125又多了一个5 所以 (5+1)*5+1=31
* 按照这个规律，则后续公式可以f(2)=f(1)*5+1 f(1)=1 则 f(x+1) = f(x)*5+1  x是5的幂次数
'''
class Solution:
	def preimageSizeFZF(self, K):
		# 确定阶梯值范围 最终的到的 base > K
		base = 1
		while base < K:
			base = base * 5 + 1

		# 确定范围后，执行精确查找
		while base > 1:
			if base-1 == K:
				return 0

			# 逆推下一个阶梯值
			base = (base - 1) / 5
			# 获取剩余值，进行下一阶梯运算
			# !!! x 里面有几个 5**base 那么 K 里面就有几个 base
			K %= base

		# 只要存在 必然是5个
		return 5