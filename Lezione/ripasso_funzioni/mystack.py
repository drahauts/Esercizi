"""
Implementa uno stack last-in-first-out (LIFO) utilizzando solo due code.
Lo stack implementato dovrebbe supportare tutte le funzioni di uno stack normale (push, top, pop e empty).

Implementa la classe MyStack:

    push(x: int) -> None: Inserisce l'elemento x in cima allo stack.
    pop() -> None: Rimuove l'elemento in cima allo stack e lo restituisce.
    top() -> None: Restituisce l'elemento in cima allo stack.
    empty() -> None: Restituisce true se lo stack è vuoto, altrimenti false.


"""

class Queue:
    pass


class MyStack:
    def __init__(self) -> None:
        self.lista = []

    def push(self, x: int) -> None:
        self.lista.append(x)

    def pop(self) -> None:
        return self.lista.pop(-1)
        

    def top(self) -> None:
        return self.lista[-1]
        

    def empty(self) -> None:
        if len(self.lista) == 0:
            return True
        else:
            return False


 	

mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())
print(mystack.pop())
