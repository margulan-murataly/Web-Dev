a=int(input())
arr= list(map(int,input().split()))
booll = False
for i in range(1,a):
    if arr[i-1]>0 and arr[i]>0 or  arr[i-1]<0 and arr[i]<0 :
        print("YES")
        booll = True
        break
if booll == False:
    print("NO")