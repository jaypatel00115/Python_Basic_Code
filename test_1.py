import math as mk

a=int(input("Enetr the value of (a)="))
b=int(input("Enetr the value of (b)="))
c=int(input("Enetr the value of (c)="))

d=b**2-4*a*c
# print(d)

if(d>0):
    print("Positive")
    ax=(-b/2*a)
    ay=mk.sqrt(d)/2*a
    r1=ax+ay
    r2=ax-ay
    print(f" root1 ={r1}")
    print(f" root 2 ={r2}")
elif(d<0):
    print("Negative")
    ax=(-b/2*a)
    ay=mk.sqrt(-d)/2*a
    # r1=ax+i(ay)
    # r2=ax-i(ay)
    # print(f" root1 ={r1}")
    # print(f" root 2 ={r2}")
    print(" Root 1 = {}+i{}".format(ax,ay))
    print(" Root 1 = {}-i{}".format(ax,ay))
else:
    print("Zero")
    ax=(-b/2*a)
    print(" Root 1 = Root 2 = {}".format(ax))
    
    