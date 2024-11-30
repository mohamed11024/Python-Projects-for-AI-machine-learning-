class RemoteControl:
    def __init__(self):
        self.channels = ["Modern Sport","Nile Sport","ON Time Sport"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


R = RemoteControl()
itr = iter(R)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
