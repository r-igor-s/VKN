a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (a>=b and a<=c) or (a<=b and a>=c):
    print(int(a))
elif b<=c and b>=a or b>=c and b<=a:
    print(int(b))
elif c>=b and c<=a or c<=b and c>=a:
    print(int(c))
else:
    print("Неможливо обчислити.")