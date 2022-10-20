import math
x = float(input("x = "))
a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))
for i in range(100):
    y = x * math.sin(x) + pow(math.e,x)
    print("% x = %.1f y = %.3f"%(i,x,y))
    x = x + h
    if x>b:
        break