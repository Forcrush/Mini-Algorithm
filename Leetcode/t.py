'''
Author: Puffrora
Date: 2019-05-04 23:31:54
LastModifiedBy: Puffrora
LastEditTime: 2020-10-17 18:55:20
'''
# 3=/76=/239=/424=/438=/480=/567=/992/1176/715=/850/968
# 466=/1248/629/493=/218=/214=/854=/1420
# https://careers.google.com/jobs/results/88312509183730374-technical-solutions-engineer-big-data-and-machine-learning/?company=Google&company=YouTube&hl=zh_CN&hl=zh_CN&jlo=en-US&location=Sydney%20NSW,%20Australia&page=3


'''
Mendeley
Zotero
'''


class Solution(object):
    def kSimilarity(self, A, B):
        from collections import deque
        
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B:
                return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)


print(Solution().kSimilarity("abccaacceecdeea", "bcaacceeccdeaae"))

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
