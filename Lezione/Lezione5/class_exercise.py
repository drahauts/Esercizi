"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called
restaurant from your class. Print the two attributes individually, and then call both methods.
"""

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type, number_served: int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"IL ristorante è {self.restaurant_name}, con la sua tipica {self.cuisine_type}")
        
    def set_number_served(self, new_client_served):
        self.number_served = new_client_served

    def increment_number_served(self, clients: int):
        self.number_served += clients
    
    def open_restaurant(self):
        print("Restourant is open!")

    def __str__(self) -> str:
        return f"Ristorante: {self.restaurant_name}, Cucina: {self.cuisine_type}, Clienti oggi: {self.number_served}"

ristorante = Restaurant(restaurant_name= "Zero Nodi", cuisine_type= "cucina Napoletana")
ristorante.describe_restaurant()
ristorante.open_restaurant()
print(ristorante)

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.
"""

ristorante_milano = Restaurant(restaurant_name= "Milan City", cuisine_type= "cucina Milanese")
ristorante_milano.describe_restaurant()
print(ristorante_milano)

mcDonalds = Restaurant(restaurant_name= "McDonalds", cuisine_type= "cucina Fast Food")
mcDonalds.describe_restaurant()
print(mcDonalds)

kebabbaro = Restaurant(restaurant_name= "Zaza", cuisine_type= "cucina Turca")
kebabbaro.describe_restaurant()
print(kebabbaro)

"""
9-3. Users: Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

class User:

    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"Name: {self.first_name}\nLastname: {self.last_name}\nAge: {self.age}\nGender: {self.gender}")
        

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def __str__(self) -> str:
        return f"User(first_name = {self.first_name}), last_name = {self.last_name}, age = {self.age}, gender = {self.gender}"

pemoluxx = User(first_name= "Danila", last_name= "Rahautsou", age= 21, gender= "M")
pemoluxx.describe_user()
pemoluxx.greet_user()
print(pemoluxx)

cr7 = User("Cristiano", "Ronaldo", 39, "M")
cr7.describe_user()
cr7.greet_user()
print(cr7)

topolino = User("Mickey", "Mouse", 777, "Non specificato")
topolino.describe_user()
topolino.greet_user()
print(topolino)


"""

9-4. Обслуженные клиенты: Начните с вашей программы из Упражнения 9-1. Добавьте атрибут с именем
number_served со значением по умолчанию 0. Создайте экземпляр с именем restaurant из этого класса.
Выведите количество клиентов, которых обслужил ресторан, а затем измените это значение и выведите его снова.
Добавьте метод с именем set_number_served(), который позволяет установить количество обслуженных клиентов.
Вызовите этот метод с новым числом и снова выведите значение. Добавьте метод с именем increment_number_served(),
который позволяет увеличить количество обслуженных клиентов. Вызовите этот метод с любым числом, которое может
представлять, сколько клиентов было обслужено, скажем, за день работы.
"""

restaurant = Restaurant(restaurant_name= "Antico Falcone", cuisine_type= "cucina Romana", number_served= 46)

print(restaurant)
restaurant.number_served = 59
print(restaurant)

"""
def set_number_served(self, new_client_served):
        self.number_served = new_client_served

    def increment_number_served(self, clients: int):
        self.number_served += clients
"""

restaurant.set_number_served(42)
print(f"Clienti oggi: {restaurant.number_served}")

restaurant.increment_number_served(12)
print(restaurant)
