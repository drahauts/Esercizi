#Danila Rahautsou
#18/04/2024

print("Hello, world!")

#2-3. Personal Message: Use a variable to represent a person’s name,
# and print a message to that person. Your message should be simple, such as,
# “Hello Eric, would you like to learn some Python today?”

name: str = input("What your name? ")
print(f"Ciao {name}, ti va di imparare un pò di Python insieme?")

# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase, uppercase, and title case.

print(name.upper(), name.title(), name.lower())

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