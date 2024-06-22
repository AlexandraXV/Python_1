class User:

    def __init__(self, first_name, last_name):
        print()
        self.first = first_name
        self.last = last_name 


    def sayName(self):
        print("Меня зовут ", self.first)
    
    def sayLast(self):
        print("Моя фамилия ", self.last)

    def sayFull(self):
        print("Вуаля ", self.first, self.last)

