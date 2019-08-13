# 基于比较的排序
# ================================
# 直接插入排序
def DirectInsertSort(a):
	for i in range(1, len(a)):
		tmp = a[i]
		j = i - 1
		while j >= 0 and a[j] > tmp:
				a[j+1] = a[j]
				j -= 1
		a[j+1] = tmp
		
	return a


# ================================
# 希尔排序
def ShellSort(a):
	step = len(a) // 2
	while step > 0:
		for i in range(step, len(a)):
			tmp = a[i]
			j = i - step
			while j >= 0 and a[j] > tmp:
				a[j+step] = a[j]
				j -= step
			a[j+step] = tmp
		step = step // 2

	return a


# ================================
# 直接选择排序
def DirectSelectSort(a):
	for i in range(0, len(a)-1):
		k = i
		for j in range(i+1, len(a)):
			if a[j] < a[k]:
				k = j
		tmp = a[i]
		a[i] = a[k]
		a[k] = tmp

	return a


# ================================
# 冒泡排序
def BubbleSort(a):
	for i in range(1, len(a)):
		flag = True
		for j in range(0, len(a)-i):
			if a[j+1] < a[j]:
				tmp = a[j]
				a[j] = a[j+1]
				a[j+1] = tmp
				flag = False
		if flag:
			break

	return a


# ================================
# 快速排序
def divide(a, low, high):
	# high = len(a) - 1
	tmp = a[low]
	while low != high:
		while low < high and a[high] > tmp:
			high -= 1
		if low < high:
			a[low] = a[high]
			low += 1
		while low < high and a[low] < tmp:
			low += 1
		if low < high:
			a[high] = a[low]
			high -= 1
	a[low] = tmp

	return low


def QuickSort(a, low, high):
	# high = len(a) - 1
	if low >= high:
		return
	mid = divide(a, low, high)
	QuickSort(a, 0, mid-1)
	QuickSort(a, mid+1, high)


# ================================
# 归并排序
def merge(a, left, mid, right):
	# right = len(a) - 1
	tmp = [0] * (right - left + 1)
	k = 0
	i = left
	j = mid
	while i < mid and j <= right:
		if a[i] < a[j]:
			tmp[k] = a[i]
			k += 1
			i += 1
		else:
			tmp[k] = a[j]
			k += 1
			j += 1
	while i < mid:
		tmp[k] = a[i]
		k += 1
		i += 1
	while j <= right:
		tmp[k] = a[j]
		k += 1
		j += 1
	m = 0
	for n in range(left, right+1):
		a[n] = tmp[m]
		m += 1


def MergeSort(a, left, right):
	if left == right:
		return
	mid = (left + right) // 2
	MergeSort(a, left, mid)
	MergeSort(a, mid+1, right)
	merge(a, left, mid+1, right)


# ================================
# 堆排序
def percolatedown(a, hole, end):
	tmp = a[hole]
	child = hole * 2 + 1
	while child <= end:
		if child < end and a[child] < a[child+1]:
			child += 1
		if a[child] > tmp:
			a[hole] = a[child]
			hole = child
			child = hole * 2 + 1
		else:
			break
	a[hole] = tmp


def HeapSort(a):
	size = len(a)
	# 初始化堆 对每个非叶节点调用向下过滤函数
	for i in range(size//2-1, -1, -1):
		percolatedown(a, i, size-1)

	for j in range(size-1, -1, -1):
		# 删除a[0] 将其移到数组末端同时堆规模减1
		a[0], a[j] = a[j], a[0]
		percolatedown(a, 0, j-1)


# 基于非比较的排序
# ================================
# 计数排序（适用于已知最大最小值的整数序列）
def CountingSort(a, amin, amax):
	b = a[:]
	# c[i]记录 i+min 出现多少次
	c = [0] * (amax-amin+1)
	for i in range(0, len(a)):
		c[a[i]-amin] += 1
	# 此时c[i]记录小于等于 i+min 的数有多少个
	for j in range(1, len(c)):
		c[j] += c[j-1]
	# 保证稳定排序
	for k in range(len(a)-1, -1, -1):
		b[c[a[k]-amin]-1] = a[k]
		c[a[k]-amin] -= 1
	for p in range(0, len(a)):
		a[p] = b[p]
	return a


# ================================
# 桶排序（适用于已知最大最小值的整数序列）
def BucketSort(a, amin, amax):
	k = 0
	# c[i]记录 i+min 出现多少次
	c = [0] * (amax-amin+1)
	for i in range(0, len(a)):
		c[a[i]-amin] += 1
	print(c)
	for j in range(0, len(c)):
		for _ in range(0, c[j]):
			a[k] = j + amin
			k += 1
			if k == len(a):
				return a


# ================================
# 基数排序（LSD-Least Significant Digital / MSD-Most Significant Digital）
def LSDRadixSort(a):
	# 初始为个位排序
	i = 0
	# 最小的位数置为1（包含0）
	n = 1
	max_num = max(a)
	# 得到最大数是几位数
	while max_num > 10**n:
		n += 1
	while i < n:
		bucket = {}
		for x in range(-9, 10):
			bucket.setdefault(x, [])
		# 对每一位进行排序
		for x in a:
			if x < 0:
				radix = -int((-x / (10**i)) % 10)
			else:
				radix = int((x / (10**i)) % 10)
			# 将对应的数组元素加入到相应位基数的桶中
			bucket[radix].append(x)
		j = 0
		for k in range(-9, 10):
			# 若桶不为空将该桶中每个元素放回到数组中
			if len(bucket[k]) != 0:
				for y in bucket[k]:
					a[j] = y
					j += 1
		i += 1


# test examples
'''
a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
DirectInsertSort(a)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
ShellSort(a)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
DirectSelectSort(a)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
BubbleSort(a)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
QuickSort(a,0,len(a)-1)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
MergeSort(a,0,len(a)-1)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
HeapSort(a)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
CountingSort(a,-1,9)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
BucketSort(a,-1,9)
print(a)

a = [1, 2, 3, 3, 5, 0, 9, 8, 5, -1]
LSDRadixSort(a)
print(a)
'''