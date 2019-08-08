class Solution:
	def firstMissingPositive(self, nums):
		if 1 not in nums:
			return 1
		if nums == [1]:
			return 2
		for i in range(len(nums)):
			if nums[i] < 1 or nums[i] > len(nums):
				nums[i] = 1
		for i in range(len(nums)):
			tmp = abs(nums[i])
			if tmp == len(nums):
				nums[0] = -abs(nums[0])
			else:
				nums[tmp] = -abs(nums[tmp])
		for i in range(1, len(nums)):
			if nums[i] > 0:
				return i
		if nums[0] < 0:
			len(nums) + 1
		else:
			return len(nums)
print(Solution().firstMissingPositive([1,1]))