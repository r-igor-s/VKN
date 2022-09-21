import math
x = float(input("Введіть х: "))
a = float(input("Введіть а: "))
b = float(input("Введіть b: "))
y = x * math.tan(x) * math.pow(math.e, a - b) + math.log(math.fabs((math.pow(x, 2) + 0.7)), 4)
print(y)