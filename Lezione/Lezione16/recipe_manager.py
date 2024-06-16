class RecipeManager:

    def __init__(self) -> None:
        self.lista_ricette: dict = {}

    def create_recipe(self, name: str, ingredients: list) -> dict:
        new_ricette: dict = {}
        """
        Crea una nuova ricetta con il nome specificato
        e una lista di ingredienti. Restituisce un dizionario
        con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
        """
        if name not in new_ricette.keys():
            new_ricette[name] = ingredients
        else:
            return 'Errore. La ricetta già esiste'

        self.lista_ricette.update(new_ricette)
        return new_ricette
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        """
        add_ingredient(recipe_name, ingredient):
        Aggiunge un ingrediente alla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio
        di errore se l'ingrediente esiste già o la ricetta non esiste.
        """
        if recipe_name in self.lista_ricette and ingredient not in self.lista_ricette[recipe_name]:
            self.lista_ricette[recipe_name].append(ingredient)
        else:
            return f'Errore. La ricetta {recipe_name} non esiste, o ingrediente {ingredient} e già presente'
        
        return self.lista_ricette
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        """
        Rimuove un ingrediente dalla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di
        errore se l'ingrediente non è presente o la ricetta non esiste.
        """
        if recipe_name in self.lista_ricette and ingredient in self.lista_ricette[recipe_name]:
            self.lista_ricette[recipe_name].remove(ingredient)
        else:
            return f'Errore. L\'ingrediente non è presente o la ricetta non esiste'
        
        return self.lista_ricette

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        """
        Sostituisce un ingrediente con un altro nella ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se
        l'ingrediente non è presente o la ricetta non esiste.
        """
        if recipe_name in self.lista_ricette and old_ingredient in self.lista_ricette[recipe_name]:
            
            for l in self.lista_ricette.values():
                print(f'Ingredienti: {l}')

            for i in range(len(l)):
                if l[i] == old_ingredient:
                    l[i] = new_ingredient
        else:
            return 'Errore.'
        
        return self.lista_ricette
    
    def list_recipes(self):
        """
        Elenca tutte le ricette esistenti.
        """
        my_key: list = []
        for key in self.lista_ricette.keys():
            my_key.append(key)
        return f'Le ricette esistenti: \n{my_key}'

    def list_ingredient(self, recipe_name: str):
        """
        Mostra gli ingredienti di una specifica ricetta.
        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
        """
        if recipe_name in self.lista_ricette:
            return f'Ingredienti in {recipe_name}:\n{self.lista_ricette[recipe_name]}'
        else:
            return f'Errore.'
        

manager = RecipeManager()
print(manager.create_recipe('Margherita', ['acqua', 'farina', 'pomodoro', 'mozzarella']))
print(manager.create_recipe('Diavola', ['acqua', 'farina', 'salame']))
print(manager.list_recipes())
print(manager.list_ingredient('Diavola'))
print(manager.list_ingredient('Margherita'))