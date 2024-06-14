class RecipeManager:

    def __init__(self) -> None:
        self.lista_ricette: dict = {}

    def create_recipe(self, name: str, ingredients: list) -> dict:
        """
        Crea una nuova ricetta con il nome specificato
        e una lista di ingredienti. Restituisce un dizionario
        con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.
        """
        if name not in self.lista_ricette.keys():
            self.lista_ricette[name] = ingredients
        else:
            return 'Errore. La ricetta già esiste'

        return self.lista_ricette
    
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
            return f'Errore. La ricetta non esiste, o ingrediente e già presente'
        
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
        if recipe_name in self.lista_ricette and old_ingredient in self.lista_ricette[recipe_name]:
            self.lista_ricette[recipe_name].remove(old_ingredient)
            self.lista_ricette[recipe_name].append(new_ingredient)
        else:
            return f'Errore. L\'ingrediente non è presente o la ricetta non esiste'
        
        return self.lista_ricette

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.add_ingredient("Pizza Margherita", "Acqua"))  
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))

