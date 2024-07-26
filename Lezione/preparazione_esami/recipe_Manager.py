"""
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
"""

class RecipeManager():
    
    def __init__(self) -> None:
        self.ricette: dict = {}
        
    def create_recipe(self, name: str, ingredients: list[str]):
        """
        - create_recipe(name, ingredients):Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
        Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore
        se la ricetta esiste già.
        """
        new_dict = {}
        if name not in self.ricette:
            new_dict[name] = ingredients
            self.ricette.update(new_dict)
            return new_dict
        else:
            return f'Errore. La ricetta esiste già'
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        """
        - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o
        la ricetta non esiste.
        """
        if recipe_name in self.ricette.keys():
            self.ricette[recipe_name].append(ingredient)
            return self.ricette
        else:
            return f'Errore.'
        
    def remove_ingredient(self, recipen_name: str, ingredient: str):
        """
        remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        """
        if recipen_name in self.ricette and ingredient in self.ricette[recipen_name]:
            self.ricette[recipen_name].remove(ingredient)
            return self.ricette
        else:
            return f'Errore.'
    
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        """
        update_ingredient(recipe_name, old_ingredient, new_ingredient):
        Sostituisce un ingrediente con un altro nella ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente
        non è presente o la ricetta non esiste.
        """
        if recipe_name in self.ricette and old_ingredient in self.ricette[recipe_name]:
            i = self.ricette[recipe_name].index(old_ingredient)
            self.ricette[recipe_name][i] = new_ingredient
            return self.ricette
        else:
            return f'Errore.'
        
    def list_recipes(self):
        """
        list_recipes(): Elenca tutte le ricette esistenti.
        """
        for k in self.ricette.keys():
            return list(str(k))
    
    def list_ingredients(self, recipe_name: str):
        if recipe_name not in self.ricette:
            return 'Errore.'
        else:
            return self.ricette[recipe_name]

    def search_recipe_by_ingredient(self, ingredient: str):
        """
        search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
        """
        ingredients = []
        for k, v in self.ricette.items():
            if ingredient in v:
                ingredients.append(k)
        return self.ricette
    

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.list_ingredients("Pizza Margherita"))
print('prova')
print(manager.search_recipe_by_ingredient('Basilico'))

