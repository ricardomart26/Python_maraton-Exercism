import string

class PhoneNumber:
    def __init__(self, number, area_code=None):
        self.number = self.convert_number(number)
        self.area_code = self.area_code(number)

    def validate_nbr_start(self, res):
        punctuation = ['@', ':', '!']
        nbr = res
        for i in nbr:
            if i.isalpha():
                raise ValueError("letters not permitted")
            if i in punctuation:
                raise ValueError("punctuations not permitted")

    def validate_nbr_end(self, res):
        if len(res) > 11:
            raise ValueError("more than 11 digits")
        if len(res) == 11:
            if res[0] != '1':
                raise ValueError("11 digits must start with 1")
            else:
                res = res[1:]
        if len(res) != 10:
            raise ValueError("incorrect number of digits")
        if res[0] in '0':
            raise ValueError("area code cannot start with zero")
        elif res[0] in '1':
            raise ValueError("area code cannot start with one")
        elif res[3] in '0':
            raise ValueError("exchange code cannot start with zero")
        elif res[3] in '1':
            raise ValueError("exchange code cannot start with one")
        return res
        
    def convert_number(self, number):
        self.validate_nbr_start(number)
        res = "".join(i for i in number if i.isdigit())
        return self.validate_nbr_end(res)

    def area_code(self, number):
        return number[:3]

    def pretty(self):
        res = ""
        save = self.number
        if len(save) == 11:
            save = save[1:]
        for i, elem in enumerate(save):
            if i == 0:
                res += "("
            elif i == 3:
                res += ")-"
            elif i == 6:
                res += "-"
            res += elem
        return res

number = PhoneNumber("(223) 456-7890")
print(number.number)

# number = PhoneNumber("123456789").number
# print(number)

# number = PhoneNumber("(023) 456-7890").number
# print(number)

