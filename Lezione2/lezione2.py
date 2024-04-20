#Danila Rahautsou
#18/04/2024

print("Hello, world!")

#2-3. Personal Message: Use a variable to represent a person’s name,
# and print a message to that person. Your message should be simple, such as,
# “Hello Eric, would you like to learn some Python today?”

your_name: str = input("What your name? ")
print(f"Ciao {your_name}, ti va di imparare un pò di Python insieme?")

# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase, uppercase, and title case.

print(your_name.upper(), your_name.title(), your_name.lower())

# 2-5. Famous Quote: Find a quote from a famous person you admire.
# Print the quote and the name of its author. Your output should look
# something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Fransce Totti una volta disse: "Nun te preoccupà, mo je faccio er cucchiaio"')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person.
# Then compose your message and represent it with a new variable called message. Print your message.

famous_person: str = "Eric Steven Raymond"
print(f'{famous_person} una volta disse: “I bravi programmatori sanno cosa scrivere. I migliori sanno cosa riscrivere.”')

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the file extension,
# like some file browsers do.

namefile: str = "python_notes.txt"
print(namefile.removesuffix(".txt"))

# 3-1. Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.

names: list = ["David", "Lucy", "Milo"]

for name in names:
    print(name)

# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.

for name in names:
    print(f"Ciao {name}, ti va di imparare un pò di Python insieme?")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
# and make a list that stores several examples. Use your list to print a series of statements about
# these items, such as “I would like to own a Honda motorcycle.”
  
my_trasport: dict = {
    "Auto" : "Seat Mii",
    "Moto" : "Ducati",
    "Bus" : "Mercedes"}

for key, values in my_trasport.items():
    print(f"Il mio veicolo di oggi è {key} e la marca è {values}")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner,
# who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

guest_list: list = ["Ronaldo", "Messi", "Mickey Mouse"]

for guest in guest_list:
    print(f"Hey, carissimo {guest}, ti invito alla mia festa. Un bacione!!!")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

print(f"Purtroppo, {guest_list[2]} ha saputo che viene {guest_list[0]} è {guest_list[1]} e ha deciso di non venire.")
guest_list[2] = "Topolino"

for guest in guest_list:
    print(f"Hey, carissimo {guest}, ti invito alla mia festa. Un bacione!!!")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guest_list.insert(0, "Vinnie the Pooh")
guest_list.insert(3, "Spider Man")
guest_list.append("Arcieri")
for guest in guest_list:
    print(f"Hey, {guest} ho trovato un TAVOLONE, SI FARÀ GRANDE FESTA!!! NON VEDO L'ORA")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

print(guest_list)
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print("Non potete capire quanto mi piange il cuore.. Il mio tavolo non arriverò mai in tempo... Tra voi posso ospitare solo 2 invitati... ")


# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person
# letting them know you’re sorry you can’t invite them to dinner.
for guest in guest_list[0:4]:
    print(f"{guest}, scusa, ma non puoi piu venire alla mia cena")
    guest_list.pop(0)

# • Print a message to each of the two people still on your list, letting them know they’re still invited.
print(f"{guest_list[0]} ricorda che sei invitato!!")
print(f"{guest_list[1]} ti aspetto stasera alla cena!!!")

# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del guest_list[0:2]

print(guest_list, len(guest_list))

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.


world = ["Japan", "USA", "Brazil", "Australia", "Messico"]
print(world)

# • Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(world))

# • Show that your list is still in its original order by printing it.
print(world)

# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(sorted(world, reverse = True))

# • Show that your list is still in its original order by printing it again.
print(world)

# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
world.reverse()
print(world)

# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
world.reverse()
print(world)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
world.sort()
print(world)

# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
world.sort(reverse = True)

# Print the list to show that its order has changed.
print(world)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating
# the number of people you’re inviting to dinner.

print(len(names))

# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains,
# rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing
# these items and then uses each function introduced in this chapter at least once.

def my_func_lesson2(my_list: list) -> list:
    for i in my_list:
        print(i.upper())
        print(i.lower())
    my_list.insert(0, "Roma")
    my_list.append("Barcelona")
    print(f"La lunghezza della mia lista adesso è {len(my_list)} ogetti")
    print(sorted(my_list))
    print(sorted(my_list, reverse = True))
    my_list.sort(reverse= True)
    print(my_list)
    my_list.pop(3)
    
    return my_list

print(my_func_lesson2(["New York", "Los Angeles", "Paris", "London", "Tokyo"]))

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

danila_dict: dict = {
    "first_name" : "Danila",
    "last_name" : "Rahautsou",
    "age" : 21,
    "city" : "Rome"
}

for keys, value in danila_dict.items():
    print(keys, value)

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_number: dict = {
    "Alice" : 5,
    "Bob" : 21,
    "Charlie" : 42,
    "Emily" : 7,
    "Jack" : 96
}

for name, num in favorite_number.items():
    print(name, num)


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and
# then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary: dict = {
    "Problem" : "A task or question that requires a solution or answer.",
    "Algorithm" : "An abstract step-by-step procedure to solve a problem.",
    "Program" : "A set of instructions telling your computer how to execute an algorithm.",
    "Data types" : "Different kinds of values that a program must represent to work with.",
    "Variables" : "Named storage locations in a program's memory, used to hold data that can be modified during program execution."
}

for key, values in glossary.items():
    print(f"In programming, the term {key} means {values}")
