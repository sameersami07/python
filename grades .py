n=int(input("enter the marks:"))
if n>=90 and n<=100:
    print("grade S ")
elif n>=80 and n<90:
    print("grade A")
elif n>=70 and n<80:
    print("grade B")
elif n>=60 and n<70:
    print("grade C")
elif n>=50 and n<60:
    print("grade D")
else:
    if n>100:
        print(" enter valid marks")
    else:
        print("fail")
        
