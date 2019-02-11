# @author - Ruben Andre Barreiro

# *** Humans' Collection Module ***

# Make sure we don't override random
import random as random_

# Make sure we don't override json
import json as json_

# Import Human's Class from Human's Module
from human import Human


# *** Humans' Collection's Class ***
class Humans_Collection:

    # Constructor
    def __init__(self):
        # Generate a random number between 1 and 10 for the total number of humans
        self.num_total_humans = random_.randint(1, 11)

        # Generate a random bit (False - 0 or True - 1) to determine which gender
        # will have their elements determined first
        gender_priority = bool(random_.getrandbits(1))

        # If gender priority is True (bit 1), the male gender will have priority
        if gender_priority:
            # Generate a random number for
            # total number of male humans between 1 and the total number of humans
            num_male_humans = random_.randint(1, self.num_total_humans)

            # The total number of female humans will be
            # the difference between the total number of humans and
            # the total number of male humans
            num_female_humans = self.num_total_humans - num_male_humans

        # If gender priority is False (bit 0), the female gender will have priority
        else:
            # Generate a random number for
            # total number of female humans between 1 and the total number of humans
            num_female_humans = random_.randint(1, self.num_total_humans)

            # The total number of male humans will be
            # the difference between the total number of humans and
            # the total number of female humans
            num_male_humans = self.num_total_humans - num_female_humans

        # Initialize the humans' array
        self.humans = []

        # Initialize the male humans' array
        self.male_humans = []

        # Initialize the female humans' array
        self.female_humans = []

        # Initialize all the possible humans' genders
        genders = ["Male", "Female"]


        # Compose the male elements and all their information
        # to be inserted in male humans' array
        with open('json/male_human_names.json') as male_names:
            male_names_data = json_.load(male_names)

            for m in range(num_male_humans):
                gender = genders[0]

                age = random_.randint(18, 91)

                male_human_index = "male_human_{index}".format(index = (m + 1))
                current_male_human_name = male_names_data[male_human_index]

                first_name = current_male_human_name["first_name"]
                last_name = current_male_human_name["last_name"]

                male_human = Human((len(self.humans) + 1),
                                first_name, last_name, gender, age)

                self.male_humans.append(male_human)
                self.humans.append(male_human)


        # Compose the female elements and all their information
        # to be inserted in female humans' array
        with open('json/female_human_names.json') as female_names:
            female_names_data = json_.load(female_names)

            for f in range(num_female_humans):
                gender = genders[1]

                age = random_.randint(18, 91)

                female_human_index = "female_human_{index}".format(index = (f + 1))
                current_female_human_name = female_names_data[female_human_index]

                first_name = current_female_human_name["first_name"]
                last_name = current_female_human_name["last_name"]

                female_human = Human((len(self.humans) + 1),
                                  first_name, last_name, gender, age)

                self.female_humans.append(female_human)
                self.humans.append(female_human)


    # *** Humans' Collection's Methods ***

    # Gets all the humans' IDs
    def getAllIDs(self):
        print("All existing Humans' IDs:")

        print("\n")
        print("IDs: [")

        for p in range(len(self.humans)):
            if(p < (len(self.humans) - 1)):
                print("        {", self.humans[p].id, "},")
            else:
                print("        {", self.humans[p].id, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male humans' IDs
    def getAllMaleIDs(self):
        print("All existing Male Humans' IDs:")

        print("\n")
        print("IDs: [")

        for m in range(len(self.male_humans)):
            if(m < (len(self.male_humans) - 1)):
                print("        {", self.male_humans[m].id, "},")
            else:
                print("        {", self.male_humans[m].id, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female humans' IDs
    def getAllFemaleIDs(self):
        print("All existing Female Humans' IDs:")

        print("\n")
        print("IDs: [")

        for f in range(len(self.female_humans)):
            if(f < (len(self.female_humans) - 1)):
                print("        {", self.female_humans[f].id, "},")
            else:
                print("        {", self.female_humans[f].id, "}")

        print("]")
        print("\n")
        print("\n")



    # Gets all the humans' First names
    def getAllFirstNames(self):
        print("All existing Humans' First Names:")

        print("\n")
        print("First Names: [")

        for p in range(len(self.humans)):
            if(p < (len(self.humans) - 1)):
                print("            {", self.humans[p].first_name, "},")
            else:
                print("            {", self.humans[p].first_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male humans' first names
    def getAllMaleFirstNames(self):
        print("All existing Male Humans' First Names:")

        print("\n")
        print("First Names: [")

        for m in range(len(self.male_humans)):
            if(m < (len(self.male_humans) - 1)):
                print("            {", self.male_humans[m].first_name, "},")
            else:
                print("            {", self.male_humans[m].first_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female humans' first names
    def getAllFemaleFirstNames(self):
        print("All existing Female Humans' First Names:")

        print("\n")
        print("First Names: [")

        for f in range(len(self.female_humans)):
            if(f < (len(self.female_humans) - 1)):
                print("            {", self.female_humans[f].first_name, "},")
            else:
                print("            {", self.female_humans[f].first_name, "}")

        print("]")
        print("\n")
        print("\n")



    # Gets all the humans' Last names
    def getAllLastNames(self):
        print("All existing Humans' Last Names:")

        print("\n")
        print("Last Names: [")

        for p in range(len(self.humans)):
            if(p < (len(self.humans) - 1)):
                print("            {", self.humans[p].last_name, "},")
            else:
                print("            {", self.humans[p].last_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the male humans' last names
    def getAllMaleLastNames(self):
        print("All existing Male Humans' Last Names:")

        print("\n")
        print("Last Names: [")

        for m in range(len(self.male_humans)):
            if(m < (len(self.male_humans) - 1)):
                print("            {", self.male_humans[m].last_name, "},")
            else:
                print("            {", self.male_humans[m].last_name, "}")

        print("]")
        print("\n")
        print("\n")

    # Gets all the female humans' last names
    def getAllFemaleLastNames(self):
        print("All existing Female Humans' Last Names:")

        print("\n")
        print("Last Names: [")

        for f in range(len(self.female_humans)):
            if(f < (len(self.female_humans) - 1)):
                print("            {", self.female_humans[f].last_name, "},")
            else:
                print("            {", self.female_humans[f].last_name, "}")

        print("]")
        print("\n")
        print("\n")




# *** Just for debug ***
# hc = Humans_Collection()


# hc.getAllIDs()
# hc.getAllMaleIDs()
# hc.getAllFemaleIDs()

# hc.getAllFirstNames()
# hc.getAllMaleFirstNames()
# hc.getAllFemaleFirstNames()
