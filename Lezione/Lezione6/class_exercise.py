"""9-1. Restaurant: Make a class called Restaurant.
The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type. Make a method called describe_restaurant()
that prints these two pieces of information, and a method called open_restaurant()
that prints a message indicating that the restaurant is open. Make an instance
called restaurant from your class. Print the two attributes individually, and then call both methods."""

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Il nome del ristorante {self.restaurant_name}, e la cucina di tipo {self.cuisine_type}")

    def open_restaurant(self):
        print("Aperto")

    def __str__(self) -> str:
        return f"Restaurant(name = {self.restaurant_name}, cucina = {self.cuisine_type})"

restaurant = Restaurant(restaurant_name="Zero Nodi", cuisine_type= "napoletana")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

"""
9-2. Three Restaurants:
Start with your class from Exercise 9-1.
Create three different instances from the class,
and call describe_restaurant() for each instance.
"""
# Crea tre diverse istanze dalla classe e chiama describe_restaurant() per ogni istanza.

ristorante1 = Restaurant(restaurant_name= "Antico Falcone", cuisine_type= "Romana")
ristorante2 = Restaurant(restaurant_name= "Arcobaleno", cuisine_type= "Olandese")
ristorante3 = Restaurant(restaurant_name= "Old Wild West", cuisine_type= "Fast Food")

ristorante1.describe_restaurant()
ristorante2.describe_restaurant()
ristorante3.describe_restaurant()

"""
9-3. Users: Make a class called User.
Create two attributes called first_name and last_name,
and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user()
that prints a summary of the user’s information. Make another
method called greet_user() that prints a personalized greeting to
the user. Create several instances representing different users, and call both methods for each user.
"""

class User:
    def __init__(self, first_name: str, last_name: str, genere: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.genere = genere
        self.age = age

    def describe_user(self):
        print(f"Utente:\nnome - {self.first_name}\ncognome - {self.last_name}\ngenere - {self.genere}\netà - {self.age}")

    def greet_user(self):
        return f"Ciao {self.first_name} {self.last_name}! Benvenuto nel nostro sito"

    def __str__(self) -> str:
        return f"User(nome= {self.first_name.capitalize()}, cognome= {self.last_name.capitalize()}, genere= {self.genere}, eta= {self.age})"


utente1 = User(first_name="Danila", last_name="Rahautsou", genere="M", age= 21)
print(utente1)
utente1.describe_user()
utente2 = User(first_name="Leo", last_name= "Messi", genere= "M", age= 35)
print(utente2)
print(utente2.greet_user())

"""
9-4. Number Served:
Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the
number of customers the restaurant has served, and then change
this value and print it again. Add a method called set_number_served()
that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any
number you like that could represent how many customers were served in, say, a day of business. 
"""

ristorante_utenti = Restaurant(restaurant_name="Stella d'Oriente", cuisine_type= "cinese", number_served= 25)
print(ristorante_utenti.number_served)