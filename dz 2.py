

#Завдання 1: Напиши програму, яка приймає від користувача рядок та повертає його в оберненому порядку з використанням службового символу \n.

рядок = input("напиши наоборот три: ")
обернений_рядок = рядок[::-1]
print(f"\nти написав це:\n{обернений_рядок}")


#Завдання 2: Напиши програму, що приймає числа від 1 до 10 та виводить їх на екран з використанням форматування f-string, додавши символ нового рядка \n після кожного числа.
for число in range(1, 6):
    print(f"{число}\n")





#Завдання 3: Маючи змінну price з числовим значенням, виведіть цю змінну у вигляді грошової суми з двома знаками після десяткової коми (наприклад, 123.45 грн).

price = float(input("напиши свою зп в $: "))
print(f"твоя зп составляє : {price:.2f} $")