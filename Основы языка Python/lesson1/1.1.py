# Задание 1
link = 'https://www.cian.ru/cat.php?bbox=44.4206520839119%2C22.451399999999992%2C65.26420880777577%2C106' \
       '.82639999999998&currency=2&deal_type=sale&engine_version=2&maxprice={}&minprice={}&offer_type=flat '
print('Добрый день!\nМы поможем Вам подобрать жильё.\n')
min_price = input('Введите цену от:')
max_price = input('Введите цену до:')
print('Можете ознакомиться с результатами поиска перейдя по ссылке:\n'+link.format(max_price, min_price))