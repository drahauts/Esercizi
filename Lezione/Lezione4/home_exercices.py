"""
8-1. Message: Write a function called display_message() that prints
one sentence telling everyone what you are learning about in this
chapter. Call the function, and make sure the message displays correctly.
"""

def display_message() -> str:
    print("Sto imparando python")

print(display_message())

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as "One of my
favorite books is Alice in Wonderland". Call the function, making sure
to include a book title as an argument in the function call.
"""

def favorite_book(book: str) -> str:
    print(f"Uno dei miei libri preferiti è {book}")

book: str = str(input("Quale il tuo libro preferito? "))
favorite_book(book)

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt.
Call the function a second time using keyword arguments.
"""

def make_shirt(size: str, text: str) -> str:
    print(f"La tua taglia è {size} è la frase che vuoi stampare è {text}")    


make_shirt("XL", "Hello world!")
make_shirt(size = "L", text= "NO TOTTI, NO PARTY")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="L", text="I love Python"):
    print(f"La tua taglia è {size} e la frase che vuoi stampare è '{text}'")

make_shirt()
make_shirt("M")
make_shirt("S", "Python is awesome!")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and
its country. The function should print a simple sentence, such as Reykjavik is in Iceland.
Give the parameter for the country a default value. Call your function for three different
cities, at least one of which is not in the default country.
"""

def describe_city(city: str, country: str = "Italy"):
    print(f"{city} è in {country}")

describe_city(city= "Napoli")
describe_city(city= "Monza")
describe_city(city= "Nizza", country= "Francia")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and
its country. The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned.
"""

def city_county(città: str, paese:str):
    return f"{città}, {paese}"

print(city_county(città= "Minsk", paese= "Bielorussia"))
print(city_county(città= "Warsawa", paese= "Poland"))
print(city_county(città= "Rio de Janeiro", paese= "Brazil"))


"""
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
The function should take in an artist name and an album title, and it should return a dictionary
containing these two pieces of information. Use the function to make three dictionaries representing
different albums. Print each return value to show that the  dictionaries are storing the album
information correctly. Use None to add an optional parameter to make_album() that allows you to store
the number of songs on an album. If the calling line includes a value for the number of songs, add that
value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
"""

def make_album(cantante: str, album: str, songs: int = None) -> dict:
    my_dict: dict = {"cantante": cantante, "album" : album}
    if songs:
        my_dict["songs"] = songs

    return my_dict

print(make_album(cantante= "Ariete", album= "Rumore"))

print(make_album("Ariete", "Rumore"))
print(make_album("Luna", "Mare", 12))
print(make_album("Stella", "Cielo"))


"""
8-8. User Albums: Start with your program from Exercise 8-7.
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, call make_album() with the user’s input and
print the dictionary that’s created. Be sure to include a quit value in the while loop.
"""

while True:
    cantante: str = input("Scrivi il tuo cantante preferito: ")
    if cantante == "quit":
        break
    album: str = input(f"Il tuo album preferito di {cantante}: ")
    songs: int = input(f"Quanti canzoni sono dentro {album}? ")
    if songs.isdigit():
        songs = int(songs)
    else:
        songs = None
    make_album(cantante, album, songs)


"""
8-9. Messages: Make a list containing a series of short text messages.
Pass the list to a function called show_messages(), which prints each text message.
"""

short_messages: list[str] = ["Come va con python?", "I LOVE C", "Dybala"]

def show_messages(l: list[str]) -> list:
    for i in l:
        print(i)

show_messages(l= short_messages)


"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves
each message to a new list called sent_messages as it’s printed. After calling the
function, print both of your lists to make sure the messages were moved correctly.
"""

def send_messages(l1: list):
    sent_messages: list[str] = []
    for i in l1:
        print(i)
        sent_messages.append(i)

lista: list[str] = ["Hello, how are you?","Forza Roma", "Playstation5 Digital Edition"]
send_messages(l1= lista)

# print(short_messages, lista)

"""
8-11. Archived Messages: Start with your work from Exercise 8-10.
Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that
the original list has retained its messages.
"""

lista1 = send_messages.copy(lista)

print(lista)
print(lista1)