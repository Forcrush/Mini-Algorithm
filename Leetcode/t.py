# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 23:31:54
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 00:43:50

def isvalid(x, y):
	if 0 <= x <= len(a[0])-1 and 0 <= y <= len(a)-1:
		return True
	else:
		return False
a=[[0,0,0,],[0,0,0]]
xdir = [1, 0, -1 ,0]
ydir = [0, -1, 0, 1]
x,y=1,1
for i in range(4):
	if isvalid(x+xdir[i],y+ydir[i]):
		print(i)
		print(a[x+xdir[i]][y+ydir[i]])