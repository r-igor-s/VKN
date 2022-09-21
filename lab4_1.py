import math
x = float(input("Вкажіть х:"))
def func(x1):
    return (x1 + math.sin(x1)) / math.log10(math.fabs(x1-math.pow(x1,4))) + math.log(x1,4)
print(func(x))
