class CricketClubs:

    # Class Attribute
    category = 'registered'

    # Initializer / Instance Attributes
    def __init__(self, name, place):
        self.name = name
        self.place = place

    # instance method
    def description(self):
        return "{} is from {} ".format(self.name, self.place)

    # instance method
    def level(self, division):
        return "{} plays in {}".format(self.name, division)


# Instantiate the CricketClubs object
turkuunited = CricketClubs("Turku United", "Turku")

# call our instance methods
print(turkuunited.description())
print(turkuunited.level("Division 1"))


# Child class (inherits from CricketClubs class)
class T20(CricketClubs):
    def team(self, status):
        return "{} has {} t20 members".format(self.name, status)


# Child class (inherits from CricketClubs class)
class SmVikko(CricketClubs):
    def team(self, status):
        return "{} has {} sm-vikko members".format(self.name, status)


# Child classes inherit attributes and
# behaviors from the parent class
turkuunited = T20("Turku United", "Turku")
print(turkuunited.description())

# Child classes have specific attributes
# and behaviors as well
print(turkuunited.team("15"))
