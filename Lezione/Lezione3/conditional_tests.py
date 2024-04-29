s1: str = "I love"
s2: str = "Python."

print("Equality and inequality tests with strings:")
print(f"Is '{s1}' equal to '{s2}'? I predict False.")
print(s1 == s2)

print(f"Is '{s1}' not equal to '{s2}'? I predict True.")
print(s1 != s2)

s_lower: str = "I LOVE"

print("\nTests using the lower() method:")
print(f"Is '{s_lower}' equal to 'love'? I predict True.")
print(s_lower.lower() == "love")

num1: int = 42
num2: int = 21

print("\nNumerical tests:")
print(f"Is {num1} greater than {num2}? I predict True.")
print(num1 > num2)

x: int = 5
y: int = 10
z: int = 15

print("\nTests using 'and' and 'or' keywords:")
print("Is x less than y and y less than z? I predict True.")
print(x < y and y < z)

print("Is x less than y or y greater than z? I predict True.")
print(x < y or y > z)


my_list: list = [1, 2, 3, 4, 5]

print("\nTest whether an item is in a list:")
print("Is 3 in the list? I predict True.")
print(3 in my_list)


print("\nTest whether an item is in a list:")
print("Is 3 in the list? I predict True.")
print(3 in my_list)

print("\nTest whether an item is not in a list:")
print("Is 6 not in the list? I predict True.")
print(6 not in my_list)
print(" ")
