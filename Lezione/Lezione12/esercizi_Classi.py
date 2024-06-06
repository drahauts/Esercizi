class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}, Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' is open!")

restaurant_1 = Restaurant("Zero Nodi", "napoletana")
restaurant_2 = Restaurant("Antico Traiano", "romana")
restaurant_3 = Restaurant("Status Quo", "vegana")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()