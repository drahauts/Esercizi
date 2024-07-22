class Movie:
    def __init__(self, movie_id : str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"Il film {self.title} è già noleggiato")

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")

class Customer:
    def __init__(self, counter_id: str, name: str) -> None:
        self.counter_id = counter_id
        self.name = name
        self.rented_movies: list[Movie] = [] # Lista dei film noleggiati
    
    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato.")
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies[movie]:
            self.rented_movies.remove(movie)
            movie.is_rented = False
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")


class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            print(f"Il film con ID {movie_id} esiste già.")
        else:
            movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie

    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            print(f"Il cliente con ID {customer_id} è già registrato.")
        else:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer

    def rent_movie(self, customer_id: str, movie_id: str):
        if movie_id not in self.movies or customer_id not in self.customers:
            print('Cliente o film non trovato.')
        else:
            if self.movies[movie_id].is_rented:
                print(f"Il film '{self.movies[movie_id].title}' è già noleggiato.")
            else:
                self.movies[movie_id].is_rented = True
                self.customers[customer_id].rented_movies.append(self.movies[movie_id])
    

    def return_movie(self, customer_id: str, movie_id: str):
        if movie_id not in self.movies or customer_id not in self.customers:
            print('Cliente o film non trovato.')
        else:
            if self.movies[movie_id] not in self.customers[customer_id].rented_movies:
                print(f"Il film '{self.movies[movie_id].title}' non è stato noleggiato da questo cliente.")
            else:
                self.customers[customer_id].rented_movies.remove(self.movies[movie_id])
                self.movies[movie_id].is_rented = False


    def get_rented_movies(self, customer_id: str):
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        else:
            print(f"Cliente non trovato.")
            return []


# Il film 'Inception' è già noleggiato.
# Il film 'Inception' non è stato noleggiato da questo cliente.


# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# # Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# # Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# # Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")