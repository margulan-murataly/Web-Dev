if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
max = premax = float('-inf')

for i in arr:
    if i>max:
        premax = max 
        max = i 
    elif i> premax and i!=max:
        premax=i
    
      
print(premax)