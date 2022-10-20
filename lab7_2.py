N = int(input("Введіть кількість рядків: "))
spisok = []
l = 0
i = 0
while i<N:
    c = input()
    i = i+1
    s = len(c)
    while s>l:
        spisok=c
        l = s
print(spisok)
