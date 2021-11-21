

class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = self.convert_matrix(matrix_string)

    def convert_matrix(self, string):
        res = []
        another_list = []
        temp = 0
        flag = False
        for i in string:
            print(i, flag, temp)
            if flag and i.isdigit():
                temp *= 10
                temp += int(i)
                print(f"Entrou aqui {temp}")
            elif flag and not i.isdigit():
                another_list.append(temp)
                flag = False
                temp = 0
            elif i.isdigit():
                temp += int(i)
                flag = True
            if i == '\n':
                res.append(another_list)
                another_list = []
        if flag:
            num = int(string[-1])
            if (len(string) > 1 and string[-2].isdigit()):
                num += (int(string[-2]) * 10)
            another_list.append(num)
        res.append(another_list)
        print(res)
        return res

    def row(self, index):
        for i, elem in enumerate(self.matrix_string):
            if i == index - 1:
                return elem


    def column(self, index):
        pass


res = Matrix("1 2 3\n4 5 6\n7 8 9")
print(res.row(2))
