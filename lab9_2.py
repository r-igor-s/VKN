A = set()
B = set()
C = set()
D = set()
for i in range(1,41):
    if i % 2 == 0:
        A.add(i)
print(f"Множина A: {A}")
for i in range(1,41):
    if i % 3 == 0:
        B.add(i)
print(f"Множина B: {B}")
for i in range(1,41):
    if i % 3 and i % 2 == 0:
        C.add(i)
print(f"Множина C: {C}")
for i in A and B:
    if i % 12 == 0:
        D.add(i)
print(f"Множина D: {D}")


