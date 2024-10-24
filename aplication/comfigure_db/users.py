class UserModel:
    def __init__(self, name: str, email: str, age: int, password: str):
        self.name = name
        self.email = email
        self.age = age
        self.password = password

class LoginUser:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

