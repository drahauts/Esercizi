class FileManager:

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        

    def __enter__(self):
        self.file_wrapper = open(self.file_name, self.mode)
        
        return self.file_wrapper

    def __exit__(self):
        self.file_wrapper.close()

with FileManager(file_name= 'prova.txt', mode= 'w') as file:

    file.write('ciao')

# with open('prova.txt', 'w') as file:

#     file.write('Ciao')

class Timer:

    def __enter__(self):
        import time
        self.time = time.time()

    def __exit__(self):
        import time

        print(f'The Elapsed: {time.time() - self.time}')

        return False

with Timer():

    import time

    time.sleep(1)