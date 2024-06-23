class Smartphone:

    def __init__(self, mark, model, number):
        print()
        self.M = mark
        self.Mo = model
        self.N = number
    
    def sayInfo(self):
        print(f"{self.M}, {self.Mo}, {self.N}")