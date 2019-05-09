class Solution:
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        result = []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        if 0 in dic and dic[0] >= 3:
            result.append([0, 0, 0])

        neg = list(filter(lambda x: x < 0, dic))
        pos = list(filter(lambda x: x>= 0, dic))
        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in dic:
                    if dif in (i, j) and dic[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < i or dif > j:
                        result.append([i, j, dif])
                    
        return result


a = [-1,-1,0,0,2,2,1,4,3,3,2]
print(Solution.threeSum(a))
