# @author - Ruben Andre Barreiro

# *** Person's Module ***


# *** Person's Class ***
class Person:

    # Constructor
    def __init__(self, id, first_name, last_name, gender, age):
        self.id = id

        self.first_name = first_name
        self.last_name = last_name

        self.gender = gender

        self.age = age

        self.is_infected = False
        self.is_dead = False


    # *** Person's Methods ***

    # Gets Person's ID
    def getID(self):
        print(self.id)

    # Sets Person's ID
    def setID(self, id):
        self.id = id

    # Gets Person's First Name
    def getFirstName(self):
        print(self.first_name)

    # Sets Person's First Name
    def setFirstName(self, id):
        self.first_name = first_name

    # Gets Person's Last Name
    def getLastName(self):
        print(self.last_name)

    # Sets Person's Last Name
    def setLastName(self, id):
        self.last_name = last_name

    # Gets Person's Gender (Male or Female)
    def getGender(self):
        print(self.gender)

    # Sets Person's Gender (Male or Female)
    def setGender(self, gender):
        self.gender = gender

    # Gets Person's Age
    def getAge(self):
        print(self.age)

    # Sets Person's Age
    def setAge(self, age):
        self.age = age

    # Gets Person's Infection Status (True - Infected or False - Not Infected)
    def getIsInfectedStatus(self):
        print(self.is_infected)

    # Sets Person's Infection Status (True - Infected or False - Not Infected)
    def setIsInfectedStatus(self, is_infected):
        if is_infected == True or is_infected == False:
            self.is_infected = is_infected

    # Gets Person's Dead Status (True - Dead or False - Not Dead)
    def getIsDeadStatus(self):
        print(self.is_dead)

    # Sets Person's Dead Status (True - Dead or False - Not Dead)
    def setIsDeadStatus(self, is_dead):
        if is_dead == True or is_dead == False:
            self.is_dead = is_dead




# *** Just for debug ***
# p = Person(1, "Ruben", "Barreiro", "Male", 26)


# p.getID()

# p.getFirstName()
# p.getLastName()

# p.getGender()

# p.getAge()

# p.getIsInfectedStatus()
# p.getIsDeadStatus()
