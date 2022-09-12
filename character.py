class Character:
    def __init__(self, name, members, weapons, magazines):
        self.name = name
        self.members = members
        self.weapons = weapons
        self.magazines = magazines
        self.alive = self.isAlive()

    def getName(self):
        return self.name

    def isAlive(self):
        for member in self.members:
            if member.isVital() and not(member.isAlive()):
                return False
        return True

    def getMembers(self):
        return self.members

    def damage(self, member, value):
        if member in self.members:
            member.damage(value)
        else:
            raise AttributeError("The given member does not belong to this character.")

    def getWeapons(self):
        return self.weapons

    def getMagazines(self):
        return self.magazines

    def __repr__(self):
        fullstr = f"{self.name}\nMembers : "
        for member in self.members:
            fullstr += member.__repr__()+'\n          '
        fullstr += "\nWeapons : "
        for weapon in self.weapons:
            fullstr += weapon.__repr__()+'\n          '
        fullstr += "\nMagazines : "
        for magazine in self.magazines:
            fullstr += magazine.__repr__()+'\n            '
        return fullstr
