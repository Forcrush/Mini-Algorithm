# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-11 13:13:39
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-11 13:31:31


'''
G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数
F(i,n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 (1 ≤ i ≤ n)


对于每个点去构建长度为 n 的二叉树
	  n
G(n)= ∑ F(i,n)
	 i=1


而对于每个点能构建长度为 n 的二叉树的数量

F(i,n) = G(i-1) * G(n-i)


即有	
	  n
G(n)= ∑ G(i-1) * G(n-i)
	 i=1

G(n) 也被称为 卡特兰数
一般的有
C_0 = 1
C_n+1 = C_n * 2(2n+1)/(n+2)
​
'''
class Solution:
	def numTrees(self, n):
		if n == 0: return 0
		tmp = 1
		for i in range(n):
			tmp = tmp*2*(2*i+1)//(i+2)
		return tmp