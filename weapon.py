class Weapon:
    def __init__(self, name, twohanded, magazine, credit_value, type, damage):
        self.name = name
        self.th = twohanded
        self.magazine = magazine
        self.value = credit_value
        self.type = type
        self.damage = damage

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getCurrentAmmo(self):
        return self.magazine.getAmount()

    def getValue(self):
        return self.value

    def isTwoHanded(self):
        return self.th

    def useAmmo(self, value):
        self.magazine.retrieve(value)

    def reload(self, value, type):
        self.magazine.addAmmo(value, type)

    def addMagazine(self, magazine):
        self.magazine.add(magazine)

    def emptyMagazine(self):
        return self.magazine.empty()

    def getDamage(self):
        return self.damage

    def __repr__(self):
        return f"Name : {self.name}, Th : {self.th}, Value : {self.value}, " \
               f"Damage : {self.damage}, Magazine : {self.magazine.__repr__()}"
