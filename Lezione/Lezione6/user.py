class User:

    def __init__(self,first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0 

    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}, age: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return f"Today user {self.first_name} {self.last_name} visited {self.login_attempts} volte our site!"
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts 


user_1 = User("Danila", "Rahautsou", 22)
user_1.describe_user()
user_1.greet_user()
print(user_1.increment_login_attempts())
print(user_1.reset_login_attempts())


class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        super().__init__(first_name, last_name, age)

        self.privileges = Privileges()


class Privileges:

    def __init__(self) -> None:
        self.privileges = ["can add post", "can delete post", "can ban user", "can take token"]

    def show_privileges(self):
        print(f"The privileges for admin {admin_1.first_name} {admin_1.last_name}: ")
        for privel in self.privileges:
            print("  ", privel)

admin_1 = Admin("Alberto", "Catoni", 20)
admin_1.privileges.show_privileges()
