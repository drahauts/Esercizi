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

    def set_number_served(self, new_user_served: int):
        self.number_served = new_user_served
    
    def increment_number_served(self, number_served: int) -> None:
        self.number_served += number_served


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
    def __init__(self, first_name: str, last_name: str, genere: str, age: int, login_attempts: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.genere = genere
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Utente:\nnome - {self.first_name}\ncognome - {self.last_name}\ngenere - {self.genere}\netà - {self.age}")

    def greet_user(self):
        return f"Ciao {self.first_name} {self.last_name}! Benvenuto nel nostro sito"
    
    def increment_login_attempts(self, increment_login: int):
        self.login_attempts += increment_login 

    def reset_login_attempts(self):
        self.login_attempts = 0 

    def __str__(self) -> str:
        return f"User(nome= {self.first_name.capitalize()}, cognome= {self.last_name.capitalize()}, genere= {self.genere}, eta= {self.age}, login_attempts = {self.login_attempts})"


utente1 = User(first_name="Danila", last_name="Rahautsou", genere="M", age= 21, login_attempts= 3)
print(utente1)
utente1.describe_user()
utente2 = User(first_name="Leo", last_name= "Messi", genere= "M", age= 35, login_attempts= 5)
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

"""
Aggiungi un metodo chiamato set_number_served() che ti permetta di impostare il numero di clienti che sono stati serviti.
"""
print(f"Clienti serviti oggi: {ristorante_utenti.number_served}")

ristorante_utenti.set_number_served(22)
print(f"Clienti serviti dopo l'impostazione: {ristorante_utenti.number_served}")

ristorante_utenti.increment_number_served(2)
print(f"Clienti serviti dopo l'incremento: {ristorante_utenti.number_served}")


"""
User
9-5. Login Attempts:
Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of
login_attempts by 1. Write another method called reset_login_attempts() that
resets the value of login_attempts to 0. Make an instance of the User class
and call increment_login_attempts() several times. Print the value of login
attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.


 Crea un'istanza della classe Utente e chiama increment_login_attempts() diverse volte.
 Stampare il valore di login_attempts per assicurarsi che sia stato incrementato correttamente,
 e poi chiamare reset_login_attempts(). Stampa di nuovo login_attempts per assicurarti che sia stato reimpostato a 0.
"""

user1 = User(first_name= "Fransceso", last_name= "Totti", genere= "M", age= 43, login_attempts= 2)
print(user1)
user1.increment_login_attempts(2)
print(f"login_attempts dopo l'incremento {user1.login_attempts}")
user1.reset_login_attempts()
print(f"dopo il reset login_attempts = {user1.login_attempts}")


"""
    9-6. Ice Cream Stand:
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant
class you wrote in Exercise 9-1  or Exercise 9-4. Either version of
the class will work; just pick the one you like better. Add an attribute
called flavors that stores a list of ice cream flavors. Write a method
that displays these flavors. Create an instance of IceCreamStand, and call this method. 

9-6. Gelateria: Una gelateria è un tipo specifico di ristorante.
Scrivi una classe chiamata IceCreamStand che eredita dalla classe
Restaurant che hai scritto nell'Esercizio 9-1 o nell'Esercizio 9-4.
Entrambe le versioni della classe funzioneranno; scegli semplicemente
quella che preferisci. Aggiungi un attributo chiamato flavors che memorizza
una lista di gusti di gelato. Scrivi un metodo che visualizza questi gusti.
Crea un'istanza di IceCreamStand e chiama questo metodo.

"""
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0, flavors: list[str] = []) -> None:
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def read_flavors(self):
        for ice in self.flavors:
            print(f"i gusti del tuo gelato sono {ice}")


    def __str__(self) -> str:
        s: str = super().__str__()[:-1]
        s += f", flavors{self.flavors}"
        return s
    
gelato = IceCreamStand(restaurant_name= "Algida", cuisine_type= "Gelateria", number_served= 12, flavors= ["amarena", "fragola", "pistacchio"])
print(gelato)
gelato.read_flavors()

"""
User
9-7. Admin:
An administrator is a special kind of user. Write a class called Admin that inherits
from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges,
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges.
Create an instance of Admin, and call your method. 
"""

class Admin(User):
    def __init__(self, first_name: str, last_name: str, genere: str, age: int, login_attempts: int, privilegies: list[str]) -> None:
        super().__init__(first_name, last_name, genere, age, login_attempts)
        self.privilegies = privilegies

    def show_priveleges(self):
        print("I priveleggi sono: ")
        for privil in self.privilegies:
            print(privil)
        
    # def __str__(self) -> str:
    #     s: str = super().__str__()[:-1]
    #     s += f", privilegies{self.privilegies}"
    #     return s
    
admin1 = Admin(first_name= "Er", last_name= "Pupone", genere= "M", age= 22, login_attempts= 1212, privilegies= ["can add post", "can delete post", "can ban user"])
print(admin1)
admin1.show_priveleges()

"""
9-8. Privilegi: Scrivi una classe separata chiamata Privileges.
La classe dovrebbe avere un attributo, privileges, che memorizza
una lista di stringhe come descritto nell'Esercizio 9-7. Sposta il
metodo show_privileges() in questa classe. Crea un'istanza di Privileges
come attributo nella classe Admin. Crea una nuova istanza di Admin e
utilizza il tuo metodo per mostrare i suoi privilegi.
"""

class Privileges:
    def __init__(self, privilegies: list[str]) -> None:
        self.privilegies = privilegies

    def show_priveleges(self):
        print("I priveleggi sono: ")
        for privil in self.privilegies:
            print(privil)

class Admin(User):
    def __init__(self, first_name: str, last_name: str, genere: str, age: int, login_attempts: int, privilegies: list[str]) -> None:
        super().__init__(first_name, last_name, genere, age, login_attempts)
        self.privilegies = Privileges(privilegies)
    

new_admin = Admin("El", "Matador", "M", 24, 22, ["can add user", "can delete user", "can block user", "can contact user"])
print(new_admin)
new_admin.privilegies.show_priveleges()