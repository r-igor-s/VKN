import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a>=b and a<=c or a<=b and a>=c:
    print(int(a))
elif b<=c and b>=a or b>=c and b<=a:
    print(int(b))
elif c>=b and c<=a or c<=b and c>=a:
    print(int(c))