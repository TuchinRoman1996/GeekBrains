def user_data(first_name, second_name, year_bern, city, email, phone):
    print(f'{second_name} {first_name}, {year_bern}г.р., г.{city}, email:{email}, тел:{phone}')


user_data(phone=input('Введите Ваш контактный телефон: '),
          email=input('Введите Ваш email: '),
          city=input('В каком городе Вы проживаете?: '),
          year_bern=input('Год Вашего рождения?: '),
          first_name=input('Введите Ваше имя: '),
          second_name=input('Введите Вашу фамилию: ')
          )
