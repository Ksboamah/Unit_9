class Dog:

    def __init__(self, name):
        self.name = name
        trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        print(self.name + " sits.")

    def lay_down(self):
        print(self.name + " lays down.")

    def roll_over(self):
        print(self.name + " rolls over.")

    def play_dead(self):
        print(self.name + " plays dead.")