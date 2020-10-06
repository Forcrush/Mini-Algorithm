# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-01 23:44:18
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-02 13:52:14



'''
Illustration:

r4	x	x	x

r3	x	x	x

r2	x	x	x

r1	x	x	x

dia	c1	c2	c3
'''
import copy


row = ['r1', 'r2', 'r3', 'r4', 'r5']
col = ['c1', 'c2', 'c3', 'r4']
dia = ['d*']

zero_puzzle = [[-1,-1,-1,1], [-1,-1,1,-1], [-1,1,-1,-1], [1,-1,-1,-1],[1,-1,-1,1]]

# True if all be 1
def check_perfect(puzzle):
	for i in range(len(puzzle)):
		for j in range(len(puzzle[0])):
			if puzzle[i][j] < 0:
				return False
	return True


def transform(puzzle, button):
	if button[0] == 'r':
		for j in range(len(puzzle[0])):
			puzzle[int(button[1])-1][j] = -puzzle[int(button[1])-1][j]
	elif button[0] == 'c':
		for i in range(len(puzzle)):
			puzzle[i][int(button[1])-1] = -puzzle[i][int(button[1])-1]
	elif button[0] == 'd':
		for k in range(min(len(puzzle[0]), len(puzzle))):
			puzzle[k][k] = -puzzle[k][k]


def find(order, best_step, cur_puzzle):
	if len(order) > 2*best_step:
		return
	elif len(order) == 2*best_step:
		if check_perfect(cur_puzzle):
			print(order)
			return
	else:
		for button in row+col+dia:
			new_puzzle = copy.deepcopy(cur_puzzle)
			transform(new_puzzle, button)
			find(order+button, best_step, new_puzzle)


find("", 5, zero_puzzle)