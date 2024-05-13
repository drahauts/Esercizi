class Room:

    def __init__(self, id: str, piano:int, seats: int) -> None:
        self.id = id
        self.piano = piano
        self.seats = seats

    def get_piano(self) -> int:
        return self.piano
    
    def get_seat(self):
        return self.seats
    
    def get_id(self):
        return self.id
    
    def __str__(self) -> str:
        return f"Room(id= {self.id}, piano = {self.piano}, seats = {self.seats})"

class Building:
    def __init__(self, name: str, adress: str, num_piani: int, room: list[Room] = []) -> None:
        self.name = name
        self.adress = adress
        self.num_piani = num_piani
        self.room : list= room

    def get_num_piani(self):
        return self.num_piani

    def get_rooms(self):
        return self.room
    
    def add_room(self, room: Room):
        if room not in self.room and room.get_piano() <= self.get_num_piani():
            self.room.append(room)

        
    def __str__(self) -> str:
        return f"{self.name.capitalize()} @{self.adress}"
    
b = Building(name="SMi", adress="Via Sierra Nevada 60", num_piani=5)
b.add_room(Room(id="666", piano=3, seats= 32))
print(b.get_rooms())