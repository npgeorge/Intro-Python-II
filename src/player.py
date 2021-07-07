# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room: List[Room] = current_room
        self.inventory = []
    
    def __str__(self):
        return f"Hello {self.name}! You are located {[self.current_room]}."

    # add the capability to add Items to the player's inventory
    # this can be a list of items in the Player class