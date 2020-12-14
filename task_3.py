month = int(input("Введите число месяца: "))

if month == 0 or month > 12:
    print("Неверный формат месяца")
else:
    # list
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]

    if month in winter:
        print("Это зима, бро")
    if month in spring:
        print("Это весна, бро")
    if month in summer:
        print("Это лето, бро")
    if month in autumn:
        print("Это осень, бро")

    # dict
    month_data = {
        'зима': [12, 1, 2],
        'весна': [3, 4, 5],
        'лето': [6, 7, 8],
        'осень': [9, 10, 11]
    }
    for m_key in month_data:
        if month in month_data[m_key]:
            print(f"Это {m_key}, бро")
            break
