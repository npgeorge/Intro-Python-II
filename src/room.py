# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def print_room(self):
        print(f'You are in {self.name}')
    def print_description(self):
        # need to pull in list with descriptions?
        print(f'Room description: {self.description}')