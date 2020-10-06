l=['1','2',['3', '4', '5'],'6',['7','8']]

res = []
def all_path(l):
	path = []
	flag = True
	for i in range(len(l)):
		if len(l[i]) == 1:
			path.extend(l[i])
		else:
			tmp1 = l[:i]
			tmp1.append(l[i][0])
			tmp1.extend(l[i+1:])
			all_path(tmp1)

			tmp2 = l[:i]
			tmp2.append(l[i][1:])
			tmp2.extend(l[i+1:])
			all_path(tmp2)

			flag = False
	if flag:
		p = ''
		for i in path:
			p += str(i)

		res.append(p)

all_path(l)
print(set(res))