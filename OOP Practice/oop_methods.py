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
