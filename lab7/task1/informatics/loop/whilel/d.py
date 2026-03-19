x =int(input())

i = 1

isItTwo = False

while i <= x:
    if (i == x):
        print("YES")
        isItTwo = True
        break
    i = i * 2


if (isItTwo == False):
    print("NO")
        