# task 5
profit_input = int(input("Пожалуйста, введите выручку: "))
costs_input = int(input("Пожалуйста, введите издержки: "))

if profit_input > costs_input:
    print("Ваша фирма работает в прибыль! Поздравляю!")
    profit = profit_input - costs_input
    profitability = (profit / profit_input) * 100
    print(f"Рентабельность выручки: {profitability}%")
    people = int(input("Введите кол-во сторудников в компании: "))
    people_profit = profit / people
    print(f"Прибыль на одного сотрудника: {people_profit}")
elif profit_input == costs_input:
    print("Ваша фирма работает в ноль!")
else:
    print("Ваша фирма работает в убыток! Ужас((")
