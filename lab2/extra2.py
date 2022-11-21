n=int(input())

def phi(n):
    if n==0 or n==1:
        return 1
    result=phi(n-1)+phi(n-2)
    return result

print(phi(n))

        