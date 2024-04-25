class UserInfo:
    def __init__(self):
        self.name = ""
        self.family = ""
        self.age = 0

    def get_info(self):
        self.name = input("Enter your name: ")
        self.family = input("Enter your family: ")
        self.age = int(input("Enter your age: "))

    def full_info(self):
        return f"Name: {self.name}, Family: {self.family}, Age: {self.age}"

user = UserInfo()
user.get_info()
print(user.full_info())