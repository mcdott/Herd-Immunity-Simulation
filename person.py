import random
random.seed(42)
from virus import Virus


class Person(object):
    """ This class contains the attributes and a method to instantiate a Person for the Simulation."""
    def __init__(self, _id, is_vaccinated, virus=None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.virus = virus
        self.is_alive = True
 

    def did_survive_infection(self, mortality_rate):
        """This method checks if a person survived an infection and are now considered vaccinated, 
        based on the virus mortality rate.""" 

        random_survival_chance = random.uniform(0.0, 1.0)
        if random_survival_chance < self.virus.mortality_rate: 
            self.is_alive = False
            return False
        else:
            self.is_vaccinated = True
            self.virus = None
            return True

if __name__ == "__main__":
    # Instantiates a vaccinated person and tests their attributes
    def test_vaccinated():
        vaccinated_person = Person(1, True)
        assert vaccinated_person._id == 1
        assert vaccinated_person.is_vaccinated is True
        assert vaccinated_person.virus is None
        assert vaccinated_person.is_alive is True

    # Instantiates an unvaccinated person and tests their attributes
    def test_unvaccinated():
        unvaccinated_person = Person(2, False)
        assert unvaccinated_person._id == 2
        assert unvaccinated_person.is_vaccinated is False
        assert unvaccinated_person.virus is None
        assert unvaccinated_person.is_alive is True

    # Instantiates an a virus object and then instantiates a person infected with that virus test their attributes
    def test_infected():
        virus = Virus("Dysentery", 0.7, 0.2)
        infected_person = Person(3, False, virus)
        assert infected_person._id == 3
        assert infected_person.is_vaccinated is False
        assert infected_person.virus == virus
        assert infected_person.is_alive is True

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    virus = Virus("Dysentery", 0.7, 0.2)
    for i in range(1, 101):
        # Instantiate 100 person objects who are infected
        i = Person(i, False, virus)
        # Append each person to the people list
        people.append(i)

    # Determine the number of people who survive the infection 
    did_survive = 0
    did_not_survive = 0
    for person in people:
        # For each person call that person's did_survive_infection method
        survived = person.did_survive_infection(person.virus.mortality_rate)
        # Count the people who survived and did not survive: 
        if survived and person.is_alive:
            did_survive += 1
        elif not survived and not person.is_alive:
            did_not_survive += 1
    total = did_survive + did_not_survive
    # Prints the results that roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 roughly 20% of the people should succumb. 
    print(f"Number who survived: {did_survive}")
    print(f"Number who did not survive: {did_not_survive}")
    print(f"Total (should be 100): {total}")
    print(f"Mortality rate: {did_not_survive / total}%")


  

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.