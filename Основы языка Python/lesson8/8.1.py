class Valid(Exception):
    def __init__(self, txt):
        self.txt = txt


class Data:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    @classmethod
    def data_converter(cls, data):
        try:
            dd = int(data.split('-')[0])
            mm = int(data.split('-')[1])
            yyyy = int(data.split('-')[2])
            return cls(dd, mm, yyyy)
        except ValueError:
            print('Только числа формата yy-mm-yyyy')

    @staticmethod
    def validator(obj):
        try:
            if 1 > obj.dd or obj.dd > 31:
                raise Valid('День должен быть в диапазоне от 1 до 31')
            elif 1 > obj.mm or obj.mm > 12:
                raise Valid('Месяц должен быть в диапазоне от 1 до 12')
            elif len(str(obj.yyyy)) < 4 or len(str(obj.yyyy)) > 4:
                raise Valid('Год должен быть четырёхзначным (например)')
        except Valid as err:
            print(err)


print(f'День: {Data.data_converter("21-11-2022").dd}')
print(f'Месяц: {Data.data_converter("21-11-2022").mm}')
print(f'Год: {Data.data_converter("21-11-2022").yyyy}')

Data.validator(Data.data_converter("21-12-20233"))
