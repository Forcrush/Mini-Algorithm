# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 16:01:01
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 16:46:25


'''
此代码不仅适用于1出现的次数,k(1-9)出现的次数都适用.

以2593为例,设k为5
从最后一位开始,cur表示当前位的值依次为3,9,5,2,high,low分别表示cur的前后,比如:
cur为9,high=25,low=3

cur = 3,high=259,low=0,[1,3]中不可能出现5,所以前缀只能取0,1,2,3...258,取不到259,所以5在个位出现了259次.
cur = 9,high = 25,low=3,[1-93]中可以出现5x,所以前缀可以0,1,2,3....25,5在10位出现了26x10=260次.
cur = 5,high = 2,low=93,[1-593]中可以出现5xx,所以前缀可以0,1,2,但是前缀为2时,5xx<=593,不是一个完整的序列,5在百位出现了2x100+93+1次,(为啥加1呢,0-93是94次,所以加1)
cur = 2,high = 0,low=593,[1-2593]中不能出现5xxx,因此5在千位0次.

总结规律:
base = 10^(i-1)
cur > k,结果为 (high+1) * base
cur == k,结果为 (high) * base + low + 1
cur < k,结果为 high * base
'''
class Solution:
	def countDigitOne(self, n):

		k = 1
		base = 1
		cnt = 0

		if n <= 0: return 0

		while n // base != 0:
			cur = (n // base) % 10
			high = n // (base * 10)
			low = n - n // base * base
			if cur > k:
				cnt += (high + 1) * base
			elif cur == k:
				cnt += high * base + low + 1
			else:
				cnt += high * base
			base *= 10

		return cnt

