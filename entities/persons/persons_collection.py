# @author - Ruben Andre Barreiro

# *** Persons' Collection Module ***

# Make sure we don't override random
import random as random_

# Make sure we don't override json
import json as json_

# Import Person's Class from Person's Module
from person import Person


# *** Persons' Collection's Class ***
class Persons_Collection:

    # Constructor
    def __init__(self):
        # Generate a random number between 1 and 10 for the total number of persons
        self.num_total_persons = random_.randint(1, 11)

        # Generate a random bit (False - 0 or True - 1) to determine which gender
        # will have their elements determined first
        gender_priority = bool(random_.getrandbits(1))

        # If gender priority is True (bit 1), the male gender will have priority
        if gender_priority:
            # Generate a random number for
            # total number of male persons between 1 and the total number of persons
            num_male_persons = random_.randint(1, self.num_total_persons)

            # The total number of female persons will be
            # the difference between the total number of persons and
            # the total number of male persons
            num_female_persons = self.num_total_persons - num_male_persons

        # If gender priority is False (bit 0), the female gender will have priority
        else:
            # Generate a random number for
            # total number of female persons between 1 and the total number of persons
            num_female_persons = random_.randint(1, self.num_total_persons)

            # The total number of male persons will be
            # the difference between the total number of persons and
            # the total number of female persons
            num_male_persons = self.num_total_persons - num_female_persons

        # Initialize the persons' array
        self.persons = []

        # Initialize the male persons' array
        self.male_persons = []

        # Initialize the female persons' array
        self.female_persons = []

        # Initialize all the possible persons' genders
        genders = ["Male", "Female"]


        # Compose the male elements and all their information
        # to be inserted in male persons' array
        with open('json/male_persons_names.json') as male_names:
            male_names_data = json_.load(male_names)

            for m in range(num_male_persons):
                gender = genders[0]

                age = random_.randint(18, 91)

                male_person_index = "male_person_{index}".format(index = (m + 1))
                current_male_person_name = male_names_data[male_person_index]

                first_name = current_male_person_name["first_name"]
                last_name = current_male_person_name["last_name"]

                male_person = Person((len(self.persons) + 1),
                                first_name, last_name, gender, age)

                self.male_persons.append(male_person)
                self.persons.append(male_person)


        # Compose the female elements and all their information
        # to be inserted in female persons' array
        with open('json/female_persons_names.json') as female_names:
            female_names_data = json_.load(female_names)

            for f in range(num_female_persons):
                gender = genders[1]

                age = random_.randint(18, 91)

                female_person_index = "female_person_{index}".format(index = (f + 1))
                current_female_person_name = female_names_data[female_person_index]

                first_name = current_female_person_name["first_name"]
                last_name = current_female_person_name["last_name"]

                female_person = Person((len(self.persons) + 1),
                                  first_name, last_name, gender, age)

                self.female_persons.append(female_person)
                self.persons.append(female_person)


    # *** Persons' Collection's Methods ***

    # Gets all the persons' IDs
    def getAllIDs(self):
        print("All existing Persons' IDs:")

        print("\n")
        print("IDs: [")

        for p in range(len(self.persons)):
            if(p < (len(self.persons) - 1)):
                print("        {", self.persons[p].id, "},")
            else:
                print("        {", self.persons[p].id, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male persons' IDs
    def getAllMaleIDs(self):
        print("All existing Male Persons' IDs:")

        print("\n")
        print("IDs: [")

        for m in range(len(self.male_persons)):
            if(m < (len(self.male_persons) - 1)):
                print("        {", self.male_persons[m].id, "},")
            else:
                print("        {", self.male_persons[m].id, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female persons' IDs
    def getAllFemaleIDs(self):
        print("All existing Female Persons' IDs:")

        print("\n")
        print("IDs: [")

        for f in range(len(self.female_persons)):
            if(f < (len(self.female_persons) - 1)):
                print("        {", self.female_persons[f].id, "},")
            else:
                print("        {", self.female_persons[f].id, "}")

        print("]")
        print("\n")
        print("\n")



    # Gets all the persons' First names
    def getAllFirstNames(self):
        print("All existing Persons' First Names:")

        print("\n")
        print("First Names: [")

        for p in range(len(self.persons)):
            if(p < (len(self.persons) - 1)):
                print("            {", self.persons[p].first_name, "},")
            else:
                print("            {", self.persons[p].first_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male persons' first names
    def getAllMaleFirstNames(self):
        print("All existing Male Persons' First Names:")

        print("\n")
        print("First Names: [")

        for m in range(len(self.male_persons)):
            if(m < (len(self.male_persons) - 1)):
                print("            {", self.male_persons[m].first_name, "},")
            else:
                print("            {", self.male_persons[m].first_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female persons' first names
    def getAllFemaleFirstNames(self):
        print("All existing Female Persons' First Names:")

        print("\n")
        print("First Names: [")

        for f in range(len(self.female_persons)):
            if(f < (len(self.female_persons) - 1)):
                print("            {", self.female_persons[f].first_name, "},")
            else:
                print("            {", self.female_persons[f].first_name, "}")

        print("]")
        print("\n")
        print("\n")



    # Gets all the persons' Last names
    def getAllLastNames(self):
        print("All existing Persons' Last Names:")

        print("\n")
        print("Last Names: [")

        for p in range(len(self.persons)):
            if(p < (len(self.persons) - 1)):
                print("            {", self.persons[p].last_name, "},")
            else:
                print("            {", self.persons[p].last_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male persons' last names
    def getAllMaleLastNames(self):
        print("All existing Male Persons' Last Names:")

        print("\n")
        print("Last Names: [")

        for m in range(len(self.male_persons)):
            if(m < (len(self.male_persons) - 1)):
                print("            {", self.male_persons[m].last_name, "},")
            else:
                print("            {", self.male_persons[m].last_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female persons' last names
    def getAllFemaleLastNames(self):
        print("All existing Female Persons' Last Names:")

        print("\n")
        print("Last Names: [")

        for f in range(len(self.female_persons)):
            if(f < (len(self.female_persons) - 1)):
                print("            {", self.female_persons[f].last_name, "},")
            else:
                print("            {", self.female_persons[f].last_name, "}")

        print("]")
        print("\n")
        print("\n")




# *** Just for debug ***
pc = Persons_Collection()


# pc.getAllIDs()
# pc.getAllMaleIDs()
# pc.getAllFemaleIDs()

# pc.getAllFirstNames()
# pc.getAllMaleFirstNames()
# pc.getAllFemaleFirstNames()
