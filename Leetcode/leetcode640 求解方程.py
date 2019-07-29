# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-26 19:04:10
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-26 20:00:07


class Solution:
	def solveEquation(self, equation):
		equa = [i for i in equation.split(' ') if i]
		clearequa = ''
		for i in equa:
			clearequa += i

		part = clearequa.split('=')
		part[0] = part[0].replace('-','/-/')
		part[0] = part[0].replace('+','/+/')
		part[1] = part[1].replace('-','/-/')
		part[1] = part[1].replace('+','/+/')
		left = [i for i in part[0].split('/') if i]
		right = [i for i in part[1].split('/') if i]

		if left[0] != '-' and left[0] != '+':
			left = ['+'] + left
		if right[0] != '-' and right[0] != '+':
			right = ['+'] + right
		
		# leftcoefficient记录x系数和 rightcoefficient记录常数和
		leftcoefficient, rightcoefficient = 0, 0

		for i in range(1, len(left)):
			if left[i] != '+' and left[i] != '-':
				# 常数项
				if 'x' not in left[i]:
					if left[i-1] == '+':
						rightcoefficient += int(left[i]) * -1
					else:
						rightcoefficient += int(left[i])
				# 含x
				else:
					if left[i-1] == '+':
						# 项为 x
						if left[i].split('x')[0] == left[i].split('x')[-1]:
							leftcoefficient += 1
						else:
							leftcoefficient += int(left[i].split('x')[0])
					else:
						# 项为 x
						if left[i].split('x')[0] == left[i].split('x')[-1]:
							leftcoefficient += -1
						else:
							leftcoefficient += int(left[i].split('x')[0]) * -1

		for i in range(1, len(right)):
			if right[i] != '+' and right[i] != '-':
				# 常数项
				if 'x' not in right[i]:
					if right[i-1] == '+':
						rightcoefficient += int(right[i])
					else:
						rightcoefficient += int(right[i]) * -1
				# 含x
				else:
					if right[i-1] == '+':
						# 项为 x
						if right[i].split('x')[0] == right[i].split('x')[-1]:
							leftcoefficient += -1
						else:
							leftcoefficient += int(right[i].split('x')[0]) * -1
					else:
						# 项为 x
						if right[i].split('x')[0] == right[i].split('x')[-1]:
							leftcoefficient += 1
						else:
							leftcoefficient += int(right[i].split('x')[0])

		# print(leftcoefficient,rightcoefficient)
		if leftcoefficient == 0 and rightcoefficient == 0:
			return 'Infinite solutions'
		elif leftcoefficient == 0 and rightcoefficient != 0:
			return 'No solution'
		else:
			return 'x=' + str(rightcoefficient//leftcoefficient)

