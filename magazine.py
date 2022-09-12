class Magazine:
    def __init__(self, amount, max_amount, type):
        self.capacity = max_amount
        self.current_amount = amount
        self.type = type

    def getType(self):
        return self.type

    def getCapacity(self):
        return self.capacity

    def getAmount(self):
        return self.current_amount

    def empty(self):
        temp = self.current_amount
        self.current_amount = 0
        return temp

    def addAmmo(self, value, type):
        if self.type == type:
            if value <= self.capacity - self.current_amount:
                self.current_amount += value
            else:
                raise ValueError("Magazine too small")
        else:
            raise TypeError("Wrong type of ammo.")

    def retrieve(self, value):
        if value <= self.current_amount:
            self.current_amount -= value
        else:
            raise ValueError("Not enough ammo or energy.")

    def merge(self, magazine):
        if self.type == magazine.getType():
            self.capacity += magazine.getCapacity()
            self.current_amount += magazine.empty()
            del magazine
        else:
            raise TypeError("Magazines are not the same type !")

    def __repr__(self):
        return f"Capacity : {self.capacity}\n" \
               f"Amount : {self.current_amount}\n" \
               f"Type : {self.type}"
