# 3=/76=/239=/424=/438=/480/567/992/1176/715/850

class Integer_Divide():
	def divide(self, num):
		res = []

		def recursion(array, rest):
			if rest == 0:
				res.append(array+[])
			for i in range(1, rest+1):
				if array == [] or (array != [] and i >= array[-1]):
					recursion(array+[i], rest-i)

		recursion([], num)

		return res

print(Integer_Divide().divide(5))