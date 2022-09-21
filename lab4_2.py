import math
x = float(input("x = "))
a = float(input("a = "))
b = float(input("b = "))
F = (math.pow(x, 2) + 0.7)
func = x * math.tan(x) * math.pow(math.e, a - b) + math.log(math.fabs(F), 4)
print(func)