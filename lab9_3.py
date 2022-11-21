workers = dict()
workers["Водень"] = "1.00794"
workers["Гелій"] = "4.002602"
workers["Літій"] = "6.941"
workers["Берилій"] = "9.012182"
workers["Бор"] = "10.811"
workers["Вуглець"] = "12.0107"
workers["Азот"] = "14.0067"
workers["Кисень"] = "15.9994"
N = int(input("Скільки записів ввести?(N): "))
for i in range(N):
    A = input("Введіть назву хімічного елемента: ")
    B = input("Введіть його атомну масу: ")
    workers[A] = B
workers_values = sorted(workers.values())
sorted_workers = dict()
for i in workers_values:
    for k in workers.keys():
        if workers[k] == i:
            sorted_workers[k] = workers[k]
            break
print(sorted_workers)
#Сортує чомусь якось не так, мабуть із-за десяткових чисел, але іншого способу я не знаю.
#Можна написати просто workers = sorted(workers.values()), але тоді на екран виведуться лише значення (атомні маси).







