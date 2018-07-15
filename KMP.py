# -*- coding: utf-8 -*-


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
    for i in range(0, slen):
        while k > -1 and p[k + 1] != s[i]:  # ptr和str不匹配，且k>-1（表示ptr和str有部分匹配）
            k = next[k]  # 往前回溯
        if p[k + 1] == s[i]:
            k = k + 1;
        if k == plen-1:  # 说明k移动到ptr的最末端
            pos.append(i-plen+1)
            k = -1  # 重新初始化，寻找下一个
            i = i - plen + 1  # i定位到该位置，外层for循环i++可以继续找下一个（这里默认存在两个匹配字符串可以部分重叠）
    return pos


a = "bacbababadababacambabacaddababacasdsd"
b = "ababaca"


print(KMP(a,b))

# ================================================================================================
# C++ code:
"""
void cal_next(char *str, int *next, int len)
{
    next[0] = -1;//next[0]初始化为-1，-1表示不存在相同的最大前缀和最大后缀
    int k = -1;//k初始化为-1
    for (int q = 1; q <= len-1; q++)
    {
        while (k > -1 && str[k + 1] != str[q])//如果下一个不同，那么k就变成next[k]，注意next[k]是小于k的，无论k取任何值。
        {
            k = next[k];//往前回溯
        }
        if (str[k + 1] == str[q])//如果相同，k++
        {
            k = k + 1;
        }
        next[q] = k;//这个是把算的k的值（就是相同的最大前缀和最大后缀长）赋给next[q]
    }
}

int KMP(char *str, int slen, char *ptr, int plen)
{
    int *next = new int[plen];
    cal_next(ptr, next, plen);//计算next数组
    int k = -1;
    for (int i = 0; i < slen; i++)
    {
        while (k >-1&& ptr[k + 1] != str[i])//ptr和str不匹配，且k>-1（表示ptr和str有部分匹配）
            k = next[k];//往前回溯
        if (ptr[k + 1] == str[i])
            k = k + 1;
        if (k == plen-1)//说明k移动到ptr的最末端
        {
            //cout << "在位置" << i-plen+1<< endl;
            //k = -1;//重新初始化，寻找下一个
            //i = i - plen + 1;//i定位到该位置，外层for循环i++可以继续找下一个（这里默认存在两个匹配字符串可以部分重叠），感谢评论中同学指出错误。
            return i-plen+1;//返回相应的位置
        }
    }
    return -1;  
}
"""