def solve():
    s = input()
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if i >= 'a' and i <= 'z':
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= cnt2:
        return(s.lower())
    else:
        return (s.upper())
print(solve())