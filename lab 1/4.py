a=int(input())
time=585
b=int(50*int(a/2)+60*int(a/2-0.5))
#print(b)
time+=b
print(int(time/60),time%60)