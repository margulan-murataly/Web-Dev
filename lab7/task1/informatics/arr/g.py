a= int(input())
arr= list(map(int,input().split()))
position = 0
for i in range(a-1):
    arr.insert(position,arr[-1])
    arr.pop(-1)
    position+=1
print(arr)