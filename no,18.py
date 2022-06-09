binary=int(input("enter number"))
i=1
d=0
while binary!=0:
    reminder=binary%10
    binary=binary//10
    d=d+reminder*i
    i=i+1
    print("decimal number",d)