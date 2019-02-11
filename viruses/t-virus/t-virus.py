# @author - Ruben Andre Barreiro

# *** T-Virus' Module ***

# Make sure we don't override time
import time as time_

# Make sure we don't override datetime
import datetime as datetime_


# *** T-Virus' Class ***
class T_Virus:

    # Constructor
    def __init__(self, id):
        now = datetime_.datetime.now()

        self.id = id

        self.type_id = 2
        self.type_name = "T-Virus"

        self.timestamp = int(round(time_.time() * 1000))
        self.date_time_creation = now.strftime("%d-%m-%Y %H:%M:%S")

        self.infectedHostPerson = None


    # *** Person's Methods ***

    # Gets T-Virus' ID
    def getID(self):
        print(self.id)

    # Sets T-Virus' ID
    def setID(self, id):
        self.id = id

    # Gets T-Virus' Virus Type ID
    def getTypeID(self):
        print(self.type_id)

    # Sets T-Virus' Virus Type ID
    def setTypeID(self, type_id):
        self.type_id = type_id

    # Gets T-Virus' Virus Type Name
    def getTypeName(self):
        print(self.type_name)

    # Sets T-Virus' Virus Type Name
    def setTypeName(self, type_name):
        self.type_name = type_name

    # Gets T-Virus' Timestamp
    def getTimestamp(self):
        print(self.timestamp)

    # Sets T-Virus' Timestamp
    def setTimetamp(self, timestamp):
        self.timestamp = timestamp

    # Gets T-Virus' Date & Time Creation
    def getDateTimeCreation(self):
        print(self.date_time_creation)

    # Sets T-Virus' Date & Creation
    def setDateTimeCreation(self, date_time_creation):
        self.date_time_creation = date_time_creation

    # Gets T-Virus' Infected Host Person
    def getInfectedHostPerson(self):
        print(self.infectedHostPerson)

    # Sets T-Virus' Infected Host Person
    def setInfectedHostPerson(self, infectedHostPerson):
        self.infectedHostPerson = infectedHostPerson

    # Gets T-Virus' Life Time in ms
    def getLifeTime(self):
        print(int(round(time_.time() * 1000)) - self.timestamp)




# *** Just for debug ***
# tv = T_Virus(1)


# tv.getID()

# tv.getTypeID()
# tv.getTypeName()

# tv.getTimestamp()
# tv.getDateTimeCreation()

# tv.getInfectedHostPerson()

# tv.getLifeTime()
