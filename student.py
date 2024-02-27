class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def checking_status(self):
        if self.mark >= 50:
            print(self.name)
            print(self.mark)
            print(f'{self.name} is passed with the mark of {self.mark}')
        else:
            print(self.name)
            print(self.mark)
            print(f"{self.name} is failed the mark of {self.mark}")