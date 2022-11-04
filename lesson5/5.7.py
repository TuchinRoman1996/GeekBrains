import json
with open('5.7.txt', 'r', encoding='utf-8') as file:
    summary = 0
    count = 0
    my_dict = {}
    loser_dict = {}
    avg_dict = {}
    for i in file:
        my_dict[i.split()[0]] = float(i.split()[2]) - float(i.split()[3])
        print(f'{i.split()[0]}, выручка составила: {my_dict[i.split()[0]]}')
        if my_dict[i.split()[0]] < 0:
            loser_dict[i.split()[0]] = my_dict[i.split()[0]]
        else:
            summary += my_dict[i.split()[0]]
            count += 1
    avg_dict['average_profit'] = summary / count
    my_list = [my_dict, loser_dict, avg_dict]
with open('file_j.json', 'w+', encoding='utf-8') as my_f:
    json.dump(my_list, my_f, ensure_ascii=False)
