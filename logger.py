
class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.logfile = file_name

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, step_number, pop_size, initial_infected, virus_name, mortality_rate, repro_rate):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.

        with open(self.logfile, "w") as logger:
            logger.writelines([f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
            f"Virus: {virus_name} \tMortality rate: {mortality_rate} \tReproduction rate: {repro_rate}\n", 
            f"\nStep {step_number}\t\tPopulation size: {pop_size}\t\tInitial number infected: {initial_infected}\n",
            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"])

    def log_interactions(self, number_of_new_infections, number_of_new_deaths, current_number_alive, total_dead, total_vaccinated):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
         with open(self.logfile, "a") as logger:
            logger.write(f"Number of new infections: {number_of_new_infections}\nNumber of new deaths: {number_of_new_deaths}\nNumber of living people: {current_number_alive}\nTotal number of deaths: {total_dead}\nTotal number of vaccinations: {total_vaccinated}\n") 

    # def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
    #     # TODO: Finish this method. If the person survives, did_die_from_infection
    #     # should be False.  Otherwise, did_die_from_infection should be True.
    #     # Append the results of the infection to the logfile
    #     pass

    def log_time_step(self, time_step_number):
        # 
        with open(self.logfile, "a") as logger:
             logger.write(f"\nTime step: {time_step_number}\n")
    
    def write_summary(self, pop_size, total_living, total_dead, number_of_vaccinations):
        why_sim_ended = "No remaining living people" if pop_size == total_dead else "Virus extinguished"
        with open(self.logfile, "a") as logger:
            logger.writelines([f"\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
            f"Why simulation ended: {why_sim_ended} "])

        with open(self.logfile, "a") as logger:
            logger.writelines([f"\n\nTotal living: {total_living} \tTotal dead: {total_dead} \tNumber of vaccinations: {number_of_vaccinations}\n",
            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"])