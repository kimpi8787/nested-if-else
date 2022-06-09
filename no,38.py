a=1500
b=2000
while a<=b:
    if a%7==0 and b%5==0:
        print(a,"divisible by 5 and 7")
    else:
        print("not divisible")
    a=a+1    