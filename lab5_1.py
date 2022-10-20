import math
x = float(input("Введіть х: "))
if x>=3.7:
    a = x + math.sqrt(x) + (4 * x + 7)**(1. / 3.)
    print (a)
elif -1.5<x and x<3.7:
    b = math.tan(x) + pow(x,2)
    print(b)
elif x<=-1.5:
    c = math.log10(math.fabs(x))
    print(c)
else:
    print("Неможливо обчислити.")