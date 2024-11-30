class Father:
    def Skills(self):
        print("Programming,Running")


class Mother:
    def Skills(self):
        Father.Skills(self)
        print("Cooking,Reading")

class Child(Father,Mother):
    def Skills(self):
        Mother.Skills(self)
        print("Games,Football player")

c = Child()
c.Skills()