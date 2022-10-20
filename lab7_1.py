slova = input("Введіть декілька слів: ")
slovo = slova.split()
slovo = min((s1 for s1 in slovo if s1), key = len)
a = slovo[::-1]
if slovo == a:
  print(f"{slovo} - паліндром.")
else:
  print(f"{slovo} не є паліндромом.")

