def Rabin_Karp(p,c):
	'''
	Rabin-Karp Algorithm -- 滚动哈希算法:
	选取两个合适的互素常数b和h（l<b<h），
	假设字符串C=c1c2c3...cm
	定义哈希函数：H(C)=(c1*b^(m-1) + c2*b^(m-2) + ... + cm*b^0) mod h
	其中b是基数，相当于把字符串看作b进制数
	字符串S=s1s2s3...sn从位置k+1开始长度为m的字符串子串S[k+1...k+m]的哈希值
	就可以利用从位置k开始的字符串子串S[k...k+m-1]的哈希值
	直接进行如下计算：H(S[k+1...k+m])=(H(S[k...k+m-1]) * b - S[k]*b^m + S[k+m]) mod h
	'''
	plen = len(p)
	clen = len(c)
	if clen > plen:
		return False
	res = []
	# hash radix
	b = 2  # 100000000007
	t = b**clen

	# 计算p和c长度为clen的前缀对应的哈希值
	phash=0
	chash=0
	for i in range(clen):
		phash = phash * b + ord(p[i])
		chash = chash * b + ord(c[i])

	# 对p不断右移一位，更新哈希值并判断
	for x in range(0, plen-clen+1):
		if phash == chash:
			res.append(x)
		if x + clen < plen:
			phash = phash*b - ord(p[x])*t + ord(p[x+clen])

	if res:
		return res
	else:
		return False


print(Rabin_Karp('abcbc','ebc')) 