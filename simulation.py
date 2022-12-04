import random, sys, math
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    """Runs the herd immunity simulation based on given inputs: virus mortality rate, population size, 
    percentage of population vaccinated, percentage of population initially infected"""
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        # Creates a Logger object to log the statistics at each step of the simulation
        self.logger = Logger('./logfile.txt')
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.virus = virus
        self.initial_infected = initial_infected
        self.population_list = self._create_population()
        self.newly_infected = []
        self.current_number_alive = pop_size
        self.total_dead = 0
        self.total_vaccinated = math.floor(self.pop_size * self.vacc_percentage)

    def _create_population(self):
        """Creates a list of people, the correct percentage of whom are vaccinated or infected."""
        population_list = []
        i = 1
        while i <= self.pop_size:
            # Add the people initially infected to the population list - Person( self, _id, is_vaccinated, is_infected)
            while i < self.initial_infected:
                person = Person(i, False, self.virus)
                population_list.append(person)
                i += 1
            # Add the people initially not infected to the population list, with the given percentage vaccinated 
            if (i - self.initial_infected) <= math.floor(self.pop_size * self.vacc_percentage):
                person = Person(i, True)
            else:
                person = Person(i, False)
            population_list.append(person)
            i += 1

        return population_list

    def _simulation_should_continue(self):
        """Returns a boolean indicating if the simulation should continue."""
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        for person in self.population_list:
            if person.is_alive == True and person.is_vaccinated == False:
                return True
        return False  

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        # Writes the starting statistics to the logger file
        time_step_counter = 0
        self.logger.write_metadata(time_step_counter, self.pop_size, self.initial_infected, self.virus.virus_name, self.virus.mortality_rate, self.virus.repro_rate)
        
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
        # This method simulates interactions between people, calulates 
        # new infections, and determines vaccinations and fatalities from infections
        # Each infected person interacts with 100 other people in the population
        number_of_interactions = 0
        number_deceased_this_step = 0
        number_recovered_from_infection_this_step = 0
        for person in self.population_list:
            # For each infected person, interact with 100 random people
            if person.virus:
                person_counter = 0
                while person_counter < 100:
                    random_person = self.population_list[random.randint(0, len(self.population_list) - 1)]
                    if random_person.is_alive == True:
                        random_living_person = random_person
                        self.interaction(random_living_person)
                        number_of_interactions += 1
                        person_counter += 1
                
                # Update the infected person's properties based on the virus' mortality rate.
                # Not dying confers immunity status of 'is_vaccinated'
                person.did_survive_infection(self.virus.mortality_rate)
                if person.is_alive == True:
                    person.is_vaccinated = True
                    number_recovered_from_infection_this_step += 1
                else:
                    number_deceased_this_step += 1
        self.total_dead += number_deceased_this_step
        self.current_number_alive -= number_deceased_this_step
        self.total_vaccinated += number_recovered_from_infection_this_step

        self.logger.log_interactions(len(self.newly_infected), number_deceased_this_step, self.current_number_alive, self.total_dead, self.total_vaccinated)
        self._infect_newly_infected()

    def interaction(self, random_living_person):
        # The possible cases covered in this method:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     a random number between 0.0 and 1.0 is generated.  If that number is smaller
            #     than repro_rate, that person is added to the newly infected array so that their 
            #     infected attribute can be changed to True at the end of the time step.
   
        if random_living_person.virus == None and random_living_person.is_vaccinated == False:
            random_infection_chance = random.uniform(0.0, 1.0)
            if random_infection_chance < self.virus.repro_rate:
                self.newly_infected.append(random_living_person)
       
    def _infect_newly_infected(self):
        # This method is called at the end of every time step to infect each newly infected person.
        # self.newly_infected is then reset back to an empty list.
        for person in self.newly_infected:
            person.virus = self.virus
            self.newly_infected.remove(person)


if __name__ == "__main__":
    # Test your simulation here
    # virus_name = "Sniffles"
    # repro_rate = 0.5
    # mortality_rate = 0.12
    # virus = Virus(virus_name, repro_rate, mortality_rate)

    # Set some values used by the simulation
    # pop_size = 1000
    # vacc_percentage = 2
    # initial_infected = 2

    # Take in parameters for the virus attributes and the population sample from the command line
    parameters = sys.argv[1:]
    pop_size = int(parameters[0])
    vacc_percentage = float(parameters[1])
    virus_name = str(parameters[2])
    mortality_rate = float(parameters[3])
    repro_rate = float(parameters[4])
    initial_infected = int(parameters[5])
    virus = Virus(virus_name, mortality_rate, repro_rate)

    # Make a new instance of the simulation
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)
    
    sim.run()
