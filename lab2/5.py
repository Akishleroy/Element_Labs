a=int(input())
s=str(a)
sum=0
for i in range(0,len(s)):
    sum+=int(s[i])*(2**(len(s)-i-1))
print(sum)