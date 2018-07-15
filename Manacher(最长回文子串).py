def manacher(s):
	
	# 对母串进行特殊处理，使其为奇数长度
	news = "#"
	for i in s:
		news += i
		news += "#"
	radius = [0] * len(news)  # 记录在新串news中以每一字符i为中心的最长回文串的半径长度，在原串s中以i为中心的最长回文串长度为radius[i]-1
	center = 0  # 记录回文串的中心
	rightboundary = 0  # 记录回文串的右边界
	finalcenter = 0  # 记录最长回文串的中心
	finalradius = 0  # 记录最长回文串的半径

	for i in range(1, len(news)):
		if i < rightboundary:
			j = 2 * center - i  # j为i关于center的对称点
			if radius[j] <= rightboundary - i:
				radius[i] = radius[j]
			else:
				radius[i] = rightboundary - i + 1
		else:
			radius[i] = 1
		while(i - radius[i] >= 0 and i + radius[i] < len(news) and news[i - radius[i]] == news[i + radius[i]]):
			radius[i] += 1
		if i + radius[i] > rightboundary:
			rightboundary = i + radius[i] - 1
			center = i

		if radius[i] > finalradius:
			finalradius = radius[i]
			finalcenter = i

	return news[finalcenter - finalradius + 1 : finalcenter + finalradius].replace("#", "")


t = "cacadada"
print(manacher(t))