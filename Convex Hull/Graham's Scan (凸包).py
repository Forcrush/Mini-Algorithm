import matplotlib.pyplot as plt 


def graham(points):

	# 若结果小于 0（k2 > k1）则 p2 能使直线 p0p1 左旋(顺时针), 反之(k2 < k1) 能使直线 p0p1 右旋(逆时针)
	crossmul = lambda p0, p1, p2 : (p2[0] - p0[0]) * (p1[1] - p0[1]) - (p1[0] - p0[0]) * (p2[1] - p0[1])

	# 两点欧氏距离
	dist = lambda p1, p2 : ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

	# 找出最左下的点(极点)
	ori_point = points[0]
	ori_pos = 0
	for i in range(1, len(points)):
		if points[i][1] < ori_point[1]:
			ori_point = points[i]
			ori_pos = i
		elif points[i][1] == ori_point[1]:
			if points[i][0] < ori_point[0]:
				ori_point = points[i]
				ori_pos = i	
	# 使极点处于第一个点
	tmp = points[0]
	points[0] = points[ori_pos]
	points[ori_pos] = tmp
	
	# 按极角从小到大距离偏短排序(顺时针)
	for i in range(1, len(points)):
		k = i
		for j in range(i + 1, len(points)):
			if crossmul(points[0], points[k], points[j]) > 0 or (crossmul(points[0], points[k], points[j]) == 0 and dist(points[k], points[0]) > dist(points[j], points[0])):
					k = j
		tmp = points[k]
		points[k] = points[i]
		points[i] = tmp


	points.append(points[0])  # 将原极点加入点集最后 实现无缝连接

	vertex = []  # 记录凸点
	saved = []  # 记录已经被存入的凸点
	vertex.append(points[0])

	#  顺时针扫描
	start = 0  # 当前射线边的起点
	end = 1  #当前射线边的终点
	while end < len(points) - 1:
		dextral = False
		# 判断是否存在点使直线右旋
		for i in range(end + 1, len(points) - 1):
			if (crossmul(points[start], points[end], points[i]) <= 0 and crossmul(points[0], points[len(points) - 2], points[i]) == 0 and i not in saved):  # 点不能使当前射线边右旋但在在最大辐角线上
				vertex.append(points[i])
				saved.append(i)
				# print(i,points[0],points[len(points) - 2],points[i],crossmul(points[0], points[len(points) - 2], points[i]),"bingo")
			if crossmul(points[start], points[end], points[i]) > 0:  # 存在点使当前射线边右旋
				dextral = True
				end = i
				break
		if dextral == False:   # 不存在点使当前射线边右旋------当前射线边一定在凸边界上
			if end not in saved:
				vertex.append(points[end])
				saved.append(end)
			start = end
			end = end + 1

	return vertex


# 可视化
def visualize(data):
	plt.xlim(xmax=10,xmin=-3)
	plt.ylim(ymax=10,ymin=-3)
	x = []
	y = []
	rx = []
	ry = []
	for i in range(0, len(data)):
		x.append(data[i][0])
		y.append(data[i][1])
	plt.plot(x, y,'ko')
	res = graham(data)
	for i in range(0, len(res)):
		rx.append(res[i][0])
		ry.append(res[i][1])
	plt.plot(rx, ry,'ro')
	plt.show()


data = [[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [4, 5], [3, 5], [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]]

visualize(data)
