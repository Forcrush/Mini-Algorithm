# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 09:01:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 09:38:53


# 基姆拉尔森计算公式 Kim larsen calculation formula
# 公元0年1月1日星期日开始 已考虑各种因素

class Solution:
	def dayOfTheWeek(self, day, month, year):
		
		def kim_larsen(day, month, year):
			
			if month < 3:
				month += 12
				year -= 1
			
			week = (day + 2*month + 3*(month + 1)//5 + year + year//4 - year//100 + year//400 + 1) % 7
			
			return week

		arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		
		return arr[kim_larsen(day, month, year)]


# 蔡勒公式 Zeller's congruence
# 要区分1582.10.4的之前和之后
# 1582.10.4之后  w = (y + y//4 + c//4 - 2*c + (26*(m+1))//10 + d - 1) % 7
# 1582.10.4及之前 w = (y + y//4 + c//4 - 2*c + (13*(m+1))//5 + d + 2) % 7;

class Solution2:
	def dayOfTheWeek(self, day, month, year):
		
		def later_date(day, month, year):
			if year > 1582:
				return True
			elif year < 1582:
				return False
			else:
				if month > 10:
					return True
				elif month < 10:
					return False
				else:
					if day > 4:
						return True
					else:
						return False

		def zeller(day, month, year):
			flag = later_date(day, month, year)
			if month < 3:
				month += 12
				year -= 1
			c = year // 100
			year = year - c * 100

			# 1582.10.4之后
			if flag:
				week = (year + year//4 + c//4 - 2*c + (26*(month+1))//10 + day - 1) % 7
			# 1582.10.4及之前
			else:
				week = (year + year//4 + c//4 - 2*c + (13*(month+1))//5 + day + 2) % 7;

			week = (week + 7) % 7
			return week

		arr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
		
		return arr[zeller(day, month, year)]

