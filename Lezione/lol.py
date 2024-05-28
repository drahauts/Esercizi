"""Если разность x1 и y1 равны разности x2 и y2. Или если суммы равны ,значит да. Иначе нет"""

x1, x2, y1, y2 = int(input()),int(input()),int(input()),int(input())
if (x1 - y1) == (x2 - y2):
    print("YES")
else:
    print("NO")