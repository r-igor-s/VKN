import math
a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))
x = a
while x <= b:
    y = x * math.sin(x) + pow(math.e,x)
    print("x = %.1f y = %.3f"%(x,y))
    x = x + h