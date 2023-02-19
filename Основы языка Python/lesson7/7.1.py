class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        output = ''
        for i in self.my_list:
            output += ''.join(str(i).strip('[]').split(','))+'\n'
        return output

    def __add__(self, other):
        new_list = []
        for i in range(len(self.my_list)):
            new_list.append([])
            for x in range(len(self.my_list[i])):
                new_list[i].append(self.my_list[i][x] + other.my_list[i][x])
        return new_list


my_list_1 = [[3, 3, 1],
             [6, 4, 2],
             [2, 3, 5]]

my_list_2 = [[5, 2, 1],
             [1, 2, 3],
             [6, 4, 3]]

my_object_1 = Matrix(my_list_1)
my_object_2 = Matrix(my_list_2)
print(my_object_1)
print(my_object_2)
print(my_object_1 + my_object_2)
