n=int(input("enter n:"))
c=n
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum=sum+r**3
if c==sum:
    print(f"it is a {sum} armstrong number")
else:
    print("it is not a armstrong number")                    
