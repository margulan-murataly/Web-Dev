def minnum(a,b,c,d):
    max =2147483647
    if a<max:
        max=a
    if b<max:
        max=b
    if c<max:
        max=c
    if d<max:
        max=d
    return max

a ,b ,c ,d =map(int, input().split())


print(minnum(a,b,c,d))