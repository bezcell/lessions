def user(
        name='Имя',
        surname='Фамилия',
        birth_year='1990',
        city='Москва',
        email='test@test.ru',
        phone='8 (999) 999 99-99'):
    return f"{surname} {name}, {birth_year} года рождения, город {city}, E-mail: {email}, Телефон: {phone}"


print(user('Игорь', 'Назаров'))
