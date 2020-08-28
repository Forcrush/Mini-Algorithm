# 3=/76=/239=/424=/438=/480=/567=/992/1176/715/850
# 466=/1248/629/493=/218=/214=/854/1420
# https://careers.google.com/jobs/results/88312509183730374-technical-solutions-engineer-big-data-and-machine-learning/?company=Google&company=YouTube&hl=zh_CN&hl=zh_CN&jlo=en-US&location=Sydney%20NSW,%20Australia&page=3


'''
Mendeley
Zotero
'''

import bisect

def max_subarray_sum(nums, k):
    arr = [0]
    cur_sum = 0
    res = float("-inf")
    for n in nums:
        cur_sum += n
        # 在 arr 里面找比 cur_sum - k 大但最接近的数
        loc = bisect.bisect_left(arr, cur_sum-k)
        # loc > len(arr) 则说明 arr 中所有数都小于 cur_sum-k
        if loc < len(arr):
            # 目前对于每次遍历 cum - array[loc] 都会是比 k 小的
            # 但是我们不仅要比 k 小还要最接近 k 因此在这些数里面找最大
            res = max(res, cur_sum-arr[loc])
        # 加入cur_sum 并且还要维护排序
        bisect.insort(arr, cur_sum)

    return res


print(max_subarray_sum([2,2,-1], 0))







def cal_next(s, length):

    next = [-1] * length  
    k = -1 
    for q in range(1, length):
        while k > -1 and s[k+1] != s[q]: 
            k = next[k]  
        if s[k + 1] == s[q]: 
            k = k + 1;
        next[q] = k; 
    return next  
def KMP(s, p):
    slen = len(s)
    plen = len(p)
    pos = []
    next = cal_next(p, plen)  
    k = -1
    i = 0
    while i < slen:
        while k > -1 and p[k + 1] != s[i]:  
            k = next[k]  
        if p[k + 1] == s[i]:
            k = k + 1;
        if k == plen-1:
            pos.append(i-plen+1)
            k = -1  
            i = i - plen + 1  
        i += 1
    return pos


a = "bababababcabababadababacambabacaddababacasdsd"
b = "ababab"


# print(KMP(a,b))