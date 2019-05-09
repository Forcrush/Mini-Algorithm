# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-05 19:26:05
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-06 00:28:10


class Solution:
    def maximumGap(self, nums):
    	if len(nums) == 1:
    		return 0
    	minval = sum(nums)
    	maxval = -1 * minval
    	for i in nums:
    		minval = min(i, minval)
    		maxval = max(i, maxval)
    	if maxval == minval:
    		return 0

    	# average distance between these numbers
		# math.ceil 向上取整
		# or there maybe: minval + avd * (len(nums) - 1) < maxval, and maxval won't be distributed in any bucket
		avd = (maxval - minval) // (len(nums) - 1) + 1

    	# number of buckets
		# math.ceil 向上取整
		# or there maybe: minval + avd * bucketnum < maxval, and maxval won't be distributed in any bucket
		bucketnum = (maxval - minval) // avd + 1

    	bucketmax = [minval-1] * bucketnum
    	bucketmin = [maxval+1] * bucketnum

    	for i in range(len(nums)):
    		if nums[i] == minval:
    			continue
    		target = (nums[i] - minval - 1) // avd
    		bucketmax[target] = max(bucketmax[target], nums[i])
    		bucketmin[target] = min(bucketmin[target], nums[i])

    	gap = 0

    	# find the first valid bucket
    	for i in range(bucketnum):
    		if bucketmax[i] != minval-1 and bucketmin[i] != maxval+1:
    			start = i
    			# since the minval is not in buckets
    			gap = max(gap, bucketmin[start] - minval)
    			break

    	for j in range(start+1, bucketnum):
    		if bucketmax[j] != minval-1 and bucketmin[j] != maxval+1:
    			gap = max(gap, bucketmin[j] - bucketmax[start])
    			start = j

    	return gap

