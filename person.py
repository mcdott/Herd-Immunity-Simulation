import random
random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated = False, virus=None):
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.virus = virus
        self.is_alive = True
 

    def did_survive_infection(self, mortality_rate):
        # This method checks if a person survived an infection. 
        # TODO Only called if infection attribute is not None.
        # Check generate a random number between 0.0 - 1.0
        # If the number is less than the mortality rate of the 
        # person's infection they have passed away. 
        # Otherwise they have survived infection and they are now vaccinated. 
        # Set their properties to show this
        # TODO: The method Should return a Boolean showing if they survived.

        random_survival_chance = random.uniform(0.0, 1.0)
        if random_survival_chance < self.virus.mortality_rate: 
            self.is_alive = False
            return False
        else:
            self.is_vaccinated = True
            self.virus = None
            return True





if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    def test_vaccinated():
        vaccinated_person = Person(1, True)
        assert vaccinated_person._id == 1
        assert vaccinated_person.is_vaccinated is True
        assert vaccinated_person.virus is None
        assert vaccinated_person.is_alive is True

    # Create an unvaccinated person and test their attributes
    def test_unvaccinated():
        unvaccinated_person = Person(2, False)
        assert unvaccinated_person._id == 2
        assert unvaccinated_person.is_vaccinated is False
        assert unvaccinated_person.virus is None
        assert unvaccinated_person.is_alive is True

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    # Create a Person object and give them the virus infection
    def test_infected():
        virus = Virus("Dysentery", 0.7, 0.2)
        infected_person = Person(3, False, virus)
        assert infected_person._id == 3
        assert infected_person.is_vaccinated is False
        assert infected_person.virus is virus
        assert infected_person.is_alive is True

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 100):
        # TODO Make a person with an infection
        # TODO Append the person to the people list
        pass

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 

    # for person in people:
    #     # For each person call that person's did_survive_infection method
    #     survived = person.did_survive_infection()

    # Count the people that survived and did not survive: 
   
    # did_survived = 0
    # did_not_survive = 0

    # TODO Loop over all of the people 
    # TODO If a person is_alive True add one to did_survive
    # TODO If a person is_alive False add one to did_not_survive

    # TODO When the loop is complete print your results.
    # The results should roughly match the mortality rate of the virus
    # For example if the mortality rate is 0.2 rough 20% of the people 
    # should succumb. 

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.