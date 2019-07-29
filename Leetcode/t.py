class Solution:
	def fourSum(self, nums, target):

		# nums 为有序数组
		def kSum(nums, target, start, k):
			res = []
			if start >= len(nums) or k > len(nums)-start:
				return res
			# 化简到两数之和问题 双指针方法
			if k == 2:
				left, right = start, len(nums)-1
				while left < right:
					if nums[left] + nums[right] == target:
						res.append([nums[left]]+[nums[right]])
						left += 1
						right -= 1

					elif nums[left] + nums[right] < target:
						left += 1
					else:
						right -= 1
					
					while left < len(nums) and nums[left] == nums[left-1]:
						left += 1
					while right >= 0 and nums[right] == nums[right+1]:
						right -= 1
				return res

			for i in range(start, len(nums)):
				if i > start and nums[i] == nums[i-1]:
					continue
				nextres = kSum(nums, target-nums[i], i+1, k-1)
				for item in nextres:
					res.append([nums[i]] + item)

			return res

		nums.sort()
		return kSum(nums, target, 0, 7)


a = [1,-1,0,0,-2,2,2,-3,1]
print(Solution().fourSum(a,0))