class Member:
    def __init__(self, name, hpvalue, isvital):
        self.name = name
        self.hp = hpvalue
        self.vital = isvital

    def getName(self):
        return self.name

    def isVital(self):
        return self.vital

    def isAlive(self):
        return self.hp > 0

    def damage(self, value):
        if self.isAlive():
            self.hp -= value
        else:
            raise ValueError("Member already dead.")

    def heal(self, value):
        if self.isAlive():
            self.hp += value
        else:
            raise ValueError("Member already dead.")

    def __repr__(self):
        return f"Name : {self.name}, Vital : {self.vital}, Hp : {self.hp}"
