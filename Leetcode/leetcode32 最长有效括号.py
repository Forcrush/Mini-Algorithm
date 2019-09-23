# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-18 17:07:42
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-18 17:47:32


# 动态规划
'''
定义一个 dp 数组，其中第 i 个元素表示以下标为 i 的字符结尾的最长有效子字符串的长度
			dp[i-2] + 2 , 当字符串形如 ......()
		/
dp[i] = 
		\
			dp[i-1] + dp[i-dp[i-1]-1] + 2 , 当字符串形如 ......))

时间复杂度： O(n)
空间复杂度： O(n)
'''	
class Solution:
	def longestValidParentheses(self, s):
		dp = [0] * (len(s))
		res = 0
		for i in range(1, len(s)):
			if s[i] == ')' and s[i-1] == '(':
				if i < 2:
					dp[i] = 2
				else:
					dp[i] = dp[i-2] + 2
			elif s[i] == ')' and s[i-1] == ')' and i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
				if i - dp[i-1] - 1 <= 1:
					dp[i] = dp[i-1] + 2
				else:
					dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2

			res = max(res, dp[i])
		return res


# 栈
'''
首先将 -1 放入栈
对于遇到的每个 '(' ，我们将它的下标放入栈中
对于遇到的每个 ')' ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，得出当前有效括号字符串的长度

时间复杂度： O(n)
空间复杂度： O(n)
'''
class Solution2:
	def longestValidParentheses(self, s):
		stack = [-1]
		res = 0
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			elif s[i] == ')':
				stack.pop()
				if stack == []:
					stack.append(i)
				else:
					res = max(res, i-stack[-1])
		return res
		

# 双向扫描
'''
首先从左到右遍历字符串，对于遇到的每个'(', 增加 left,对于遇到的每个')', 增加 rightright
每当 left 与 right相等时, 计算当前有效字符串的长度，并且记录目前为止找到的最长子字符串
如果 right比 left大时，将 left 和 right 同时置零

再类似地从右到左遍历字符串

时间复杂度： O(n)
空间复杂度： O(1)
'''
class Solution3:
	def longestValidParentheses(self, s):
		res = 0
		left, right = 0, 0
		for i in range(len(s)):
			if s[i] == '(':
				left += 1
			elif s[i] == ')':
				right += 1
			if left == right:
				res = max(res, left*2)
			if right > left:
				left, right = 0, 0

		left, right = 0, 0
		for i in range(len(s)-1, -1, -1):
			if s[i] == '(':
				left += 1
			elif s[i] == ')':
				right += 1
			if left == right:
				res = max(res, left*2)
			if right < left:
				left, right = 0, 0

		return res

