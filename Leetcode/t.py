def count1(n):
    res = 0
    while n != 0:
        n &= n - 1
        res += 1
    return res

print(count1(32))