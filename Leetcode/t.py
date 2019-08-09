class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		pool = set()
		for i in range(len(nums)):
			if nums[i] in pool:
				return True
			else:
				pool.add(nums[i])
			print(len(pool))
			if len(pool) > k:
				print('exceed')
				pool.remove(nums[i-k])
		return False

print(Solution().containsNearbyDuplicate([1,2,3,1],2))