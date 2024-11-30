class Car:
    def __init__(self , name , color , version):
        self.name = name
        self.type = color
        self.version = int(version)

    def move(self):
        if self.name == "mercedes":
            print(self.name , "can move more quick")
        elif self.name == "toyota":
            print(self.name , "can move less quick from merceds")


mercedes = Car("mercedes","black",2016)
mercedes.move()            