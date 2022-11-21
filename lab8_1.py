from array import *

M = int(input("Введіть число M: "))
N = input("Введіть числа N через кому: ")
n1 = N.split(",")
kratne = array('i', [])
for elem in n1:
    elem = int(elem)
    if M % elem == 0:
       kratne.append(elem)
print(kratne)