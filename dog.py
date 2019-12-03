class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        self.trick_list.append("sits")
        print(self.name + " sits.")

    def lay_down(self):
        self.trick_list.append("lays down")
        print(self.name + " lays down.")

    def roll_over(self):
        self.trick_list.append("rolls over")
        print(self.name + " rolls over.")

    def play_dead(self):
        self.trick_list.append("plays dead")
        print(self.name + " plays dead.")

    def print_trick_list(self):
        if self.trick_list == []:
            print(self.name + " has not performed any tricks.")
        else:
            print(self.name + " has performed the following tricks:")
        for x in self.trick_list:
            print(x)