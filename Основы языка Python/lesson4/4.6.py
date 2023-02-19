from itertools import count, cycle

my_list = []
for i in count(0, 50):
    if i > 1000:
        break
    else:
        my_list.append(i)

for x in cycle(my_list):
    if x > 600:
        break
    else:
        print(x)
