# 3=/76=/239=/424=/438=/480=/567/992/1176/715/850
# 421
# https://careers.google.com/jobs/results/88312509183730374-technical-solutions-engineer-big-data-and-machine-learning/?company=Google&company=YouTube&hl=zh_CN&hl=zh_CN&jlo=en-US&location=Sydney%20NSW,%20Australia&page=3

def cal_next(s, length):

    next = [-1] * length  # next[0]初始化为-1，-1表示不存在相同的最大前缀和最大后缀
    k = -1  # k初始化为-1
    for q in range(1, length):
        while k > -1 and s[k+1] != s[q]:  # 如果下一个不同，那么k就变成next[k]，注意next[k]是小于k的，无论k取任何值。
            k = next[k]  # 往前回溯
        if s[k + 1] == s[q]:  # 如果相同，k++
            k = k + 1;
        next[q] = k;  # 这个是把算的k的值（就是相同的最大前缀和最大后缀长）赋给next[q]
    return next  # next[i]表示长度为 i+1 的串相同最大前缀/最大后缀长为 next[i]+1


def KMP(s, p):  # s 原串  p 子串
    slen = len(s)
    plen = len(p)
    pos = []
    next = cal_next(p, plen)  # 计算next数组
    k = -1
    i = 0
    while i < slen:
        while k > -1 and p[k + 1] != s[i]:  # ptr和str不匹配，且k>-1（表示ptr和str有部分匹配）
            k = next[k]  # 往前回溯
        if p[k + 1] == s[i]:
            k = k + 1;
        if k == plen-1:  # 说明k移动到ptr的最末端
            pos.append(i-plen+1)
            k = -1  # 重新初始化，寻找下一个
            i = i - plen + 1  # i定位到该位置，外层for循环i++可以继续找下一个（这里默认存在两个匹配字符串可以部分重叠）
        i += 1
    return pos


a = "bababababcabababadababacambabacaddababacasdsd"
b = "ababab"


print(KMP(a,b))