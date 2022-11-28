import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    """Runs the herd immunity simulation based on given inputs: virus mortality rate, population size, 
    percentage of population vaccinated, percentage of population initially infected"""
    def __init__(self, virus_name, repro_rate, mortality_rate, pop_size, vacc_percentage, initial_infected=1):
        # Creates a Logger object to log the statistics at each step of the simulation
        self.logger = Logger('./logfile.txt')
        # >>>>>
        # logger = open(self.logger.logfile, "w")
        # logger.write("testing...")
        # with open(self.logger.logfile, "w") as logger:
        #     logger.write("testing2...")

        #>>>>>>>>>>>FIGURE OUT HOW TO ACCESS VIRUS ATTRIBUTES AND CLEAN THIS UP
        self.virus_name = virus_name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population_list = self._create_population()
        self.newly_infected = []

    def _create_population(self):
        """Creates a list of people, the correct percentage of whom are vaccinated or infected."""
        population_list = []
        i = 1
        while i <= self.pop_size:
            # Add the people initially infected to the population list - Person( self, _id, is_vaccinated, is_infected)
            while i < self.initial_infected:
                person = Person(i, False, True)
                population_list.append(person)
                i += 1
            # Add the people initially not infected to the population list, with the given percentage vaccinated 
            if (i - self.initial_infected) <= (self.pop_size * self.vacc_percentage / 100):
                person = Person(i, True, False)
            else:
                person = Person(i, False, False)
            population_list.append(person)
            i += 1

        # for person in population_list:
        #     print(f"{person._id} {person.is_vaccinated} {person.is_infected}")
        return population_list

    def _simulation_should_continue(self):
        """Returns a boolean indicating if the simulation should continue."""
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        for person in self.population_list:
            # print(f">>>{person._id} {person.is_alive} {person.is_vaccinated}")
            if person.is_alive == True and person.is_vaccinated == False:
                return True
        return False  

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        # Writes the starting statistics to the logger file
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.initial_infected, self.virus_name, self.mortality_rate, self.repro_rate)
        
        time_step_counter = 0
        should_continue = True
        while should_continue:
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            self.time_step()
            should_continue = self._simulation_should_continue()
            print(f"Should continue: >> {should_continue}")


        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        number_of_interactions = 0
        number_deceased_this_step = 0
        number_recovered_from_infection_this_step = 0
        for person in self.population_list:
            # For each infected person, interact with 100 random people
            if person.is_infected == True:
                person_counter = 0
                while person_counter < 100:
            # >>>>>>>>>THIS WILL CREATE AN INFINITE LOOP IF THERE ARE FEWER THAN 100 PEOPLE ALIVE!!! 
            # >>>>>>>>>CHECK THAT THERE ARE MORE THAN 100 PEOPLE ALIVE BEFORE STARTING THIS LOOP
                    random_person = self.population_list[random.randint(0, len(self.population_list) - 1)]
                    if random_person.is_alive == True:
                        random_living_person = random_person
                        self.interaction(random_living_person)
                        number_of_interactions += 1
                        person_counter += 1
                
                # Update the infected person's properties based on the virus' mortality rate.
                # Not dying confers immunity status of 'is_vaccinated'
                person.did_survive_infection(self.mortality_rate)
                if person.is_alive == True:
                    number_recovered_from_infection_this_step += 1
                else:
                    number_deceased_this_step += 1


        self.logger.log_interactions(number_of_interactions, len(self.newly_infected), number_recovered_from_infection_this_step, number_deceased_this_step)
        self._infect_newly_infected()




    def interaction(self, random_living_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
   
        if random_living_person.is_infected == False and random_living_person.is_vaccinated == False:
            random_infection_chance = random.uniform(0.0, 1.0)
            if random_infection_chance < self.repro_rate:
                self.newly_infected.append(random_living_person)

        # TODO: Call logger method during this method.
  
     

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.is_infected = True
            self.newly_infected.remove(person)


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_rate = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_rate, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 2
    initial_infected = 2

    # Make a new instance of the simulation
    sim = Simulation(virus.virus_name, virus.repro_rate, virus.mortality_rate, pop_size, vacc_percentage, initial_infected)
    

    sim.run()
