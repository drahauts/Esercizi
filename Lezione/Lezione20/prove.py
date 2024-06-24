# def ciao(name):
    
#     print(f'Ciao {name}')


# def salve(name):
#     print(f'Salve {name}')

# def saluta_bob(func) -> str:
#     func('Bob')

# print(saluta_bob(ciao))
# saluta_bob(salve)

# def parent():

#     print('Sono in parent!')

#     def first_child():
#         print('Sono in First Child!')
        
#     return first_child

    
#     second_child()
#     second_child()
#     first_child()

# parent()

def decorator(func):
    def wrapper():
        import time

        start = time.time()
        func()
        print(f'Time elapsed: {time.time() - start}')
    return wrapper

def say_whee():
    print('whee!')

say_whee = decorator(say_whee)

say_whee()
