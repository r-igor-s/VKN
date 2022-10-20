import math
a = float(input("a = "))
b = float(input("b = "))
h = float(input("h = "))
x = a
spisok = []
while x <= b:
    y = x * math.sin(x) + pow(math.e,x)
    x = x + h
    spisok.append(y)
print(spisok)
spisok.sort(reverse=True)
print("Список за зростанням:",spisok)