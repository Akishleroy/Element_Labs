a, b, c= input().split()
result=0

def election(a,b,c):
    if a==b:
        return a
    elif b==c:
        return b
    return a

result=election(a,b,c)
print(result)
