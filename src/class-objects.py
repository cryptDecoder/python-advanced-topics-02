class Student():

    def __init__(self, id, marks):
        self.name = "John"
        self.id = id
        self.marks = marks
        pass

    def printName(self):
        print(f"id : {self.id}")
        print(f"name is {self.name}")
        print(f"marks : {self.marks}")


std_obj = Student(10, 65)
if __name__ == '__main__':
    print("Hello python")
    std_obj.printName()
    pass
