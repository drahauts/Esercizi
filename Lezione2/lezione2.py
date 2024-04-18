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
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print(guest_list)
print("Non potete capire quanto mi piange il cuore.. Il mio tavolo non arriverò mai in tempo... Tra voi posso ospitare solo 2 invitati... ")

i = 0
while i < 4:
    print(f"{guest_list[i]}, scusa, ma non puoi piu venire alla mia cena")
    i += 1


print(guest_list)