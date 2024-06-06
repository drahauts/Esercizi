class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.restaurant_name}, Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant '{self.restaurant_name}' is open!")

    def set_number_served(self, new_served: int):
        self.number_served = new_served

    def increment_num_served(self, increment: int):
        self.number_served += increment

restaurant_1 = Restaurant("Zero Nodi", "napoletana")
restaurant_2 = Restaurant("Antico Traiano", "romana")
restaurant_3 = Restaurant("Status Quo", "vegana")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant_1.set_number_served(4)
print(restaurant_1.number_served)
restaurant_1.increment_num_served(15)
print(restaurant_1.number_served)


class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name: str, cuisine_type: str):
        super().__init__(restaurant_name, cuisine_type)

        self.flavors: list[str] = []

    def show_flavors(self):
        print("I gusti sono: ")
        for flavor in self.flavors:
            print("  ", flavor)
    

ice = IceCreamStand("Yolo", "gelateria")
ice.flavors = ["pistacchio", "nutella", "amarena"]
ice.show_flavors()