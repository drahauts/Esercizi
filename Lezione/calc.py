def calcolatrice(x, y):
    simbolo: str = input("Che tipo di operazione desideri eseguire? (+,-,*,/)")

    if simbolo == "+":
        return x + y
    elif simbolo == "-":
        return x - y
    elif simbolo == "*":
        return x * y
    elif simbolo == "/":
        if y == 0:
            return f"Divisione per zero"
        else:
            return x / y

x: float = float(input())
y: float = float(input())
print(calcolatrice(x, y))