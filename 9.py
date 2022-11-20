a = int(input())
b = int(input())
c = int(input())

if a==b:
    if b==c:
        print(3)
        exit(0)
    else:
        print(2)
        exit(0)
if b==c:
    if b==a:
        print(3)
        exit(0)
    else:
        print(2)
        exit(0)
if a==c:
    if b==a:
        print(3)
        exit(0)
    else:
        print(2)
        exit(0)
print(0)
