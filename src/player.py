# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room: List[Room] = current_room
    
    def __str__(self):
        return f"Hello {self.name}! You are located {[self.current_room]}."