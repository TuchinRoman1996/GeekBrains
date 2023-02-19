my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('5.4.txt', 'r+', encoding='utf-8') as file, \
        open('5.4_2.txt', 'w', encoding='utf-8') as file_2:
    my_arr = [my_dict[i.split()[0]]+' '+' '.join(i.split()[1:]) for i in file]
    for i in my_arr:
        file_2.writelines(i+'\n')
