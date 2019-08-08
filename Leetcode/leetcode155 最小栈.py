# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-06 22:42:14
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-06 22:54:58


'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''
class MinStack:

	def __init__(self):
		self.datastack = []
		self.minstack = []


	def push(self, x):
		self.datastack.append(x)
		if self.minstack:
			if x < self.minstack[-1]:
				self.minstack.append(x)
			else:
				self.minstack.append(self.minstack[-1])
		else:
			self.minstack.append(x)
		

	def pop(self):
		if self.datastack:
			self.minstack.pop()
		return self.datastack.pop()


	def top(self):
		if self.datastack:
			return self.datastack[-1]


	def getMin(self):
		if self.datastack:
			return self.minstack[-1]

