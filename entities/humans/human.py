# @author - Ruben Andre Barreiro

# *** Human's Module ***


# *** Human's Class ***
class Human:

    # Constructor
    def __init__(self, id, first_name, last_name, gender, age):
        self.id = id

        self.first_name = first_name
        self.last_name = last_name

        self.gender = gender

        self.age = age

        self.is_infected = False
        self.is_dead = False


    # *** Human's Methods ***

    # Gets Human's ID
    def getID(self):
        print(self.id)

    # Sets Human's ID
    def setID(self, id):
        self.id = id

    # Gets Human's First Name
    def getFirstName(self):
        print(self.first_name)

    # Sets Human's First Name
    def setFirstName(self, id):
        self.first_name = first_name

    # Gets Human's Last Name
    def getLastName(self):
        print(self.last_name)

    # Sets Human's Last Name
    def setLastName(self, id):
        self.last_name = last_name

    # Gets Human's Gender (Male or Female)
    def getGender(self):
        print(self.gender)

    # Sets Human's Gender (Male or Female)
    def setGender(self, gender):
        self.gender = gender

    # Gets Human's Age
    def getAge(self):
        print(self.age)

    # Sets Human's Age
    def setAge(self, age):
        self.age = age

    # Gets Human's Infection Status (True - Infected or False - Not Infected)
    def getIsInfectedStatus(self):
        print(self.is_infected)

    # Sets Human's Infection Status (True - Infected or False - Not Infected)
    def setIsInfectedStatus(self, is_infected):
        if is_infected == True or is_infected == False:
            self.is_infected = is_infected

    # Gets Human's Dead Status (True - Dead or False - Not Dead)
    def getIsDeadStatus(self):
        print(self.is_dead)

    # Sets Human's Dead Status (True - Dead or False - Not Dead)
    def setIsDeadStatus(self, is_dead):
        if is_dead == True or is_dead == False:
            self.is_dead = is_dead




# *** Just for debug ***
# h = Human(1, "Ruben", "Barreiro", "Male", 26)


# h.getID()

# h.getFirstName()
# p.getLastName()

# h.getGender()

# h.getAge()

# h.getIsInfectedStatus()
# h.getIsDeadStatus()
