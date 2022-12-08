from datetime import date

class Logger(object):
    def __init__(self, file_name):
        self.logfile = file_name


    def write_metadata(self, step_number, pop_size, initial_infected, virus_name, mortality_rate, repro_rate):
        """Creates the logfile and logs the metadata for the simulation at the top of the file"""
        with open(self.logfile, "w") as logger:
            logger.writelines([f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
            f"Simulation date: {date.today()}\n\n",
            f"Virus: {virus_name} \tMortality rate: {mortality_rate} \tReproduction rate: {repro_rate}", 
            f"\nStep {step_number}\t\tPopulation size: {pop_size}\t\tInitial number infected: {initial_infected}\n",
            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"])

    def log_interactions(self, number_of_new_infections, number_of_new_deaths, current_number_alive, total_dead, total_vaccinated):
        """Logs the interactions to the logfile"""
        with open(self.logfile, "a") as logger:
            logger.write(f"Number of new infections: {number_of_new_infections}\nNumber of new deaths: {number_of_new_deaths}\nNumber of living people: {current_number_alive}\nTotal number of deaths: {total_dead}\nTotal number of vaccinations: {total_vaccinated}\n") 


    def log_time_step(self, time_step_number):
        """Logs the time step number to the logfile"""
        with open(self.logfile, "a") as logger:
             logger.write(f"\nTime step: {time_step_number}\n")
    
    def write_summary(self, time_step_number, pop_size, total_living, total_dead, number_of_vaccinations, number_of_interactions, times_a_vaccination_protected_a_person):
        """Logs the summary of the simulation to the bottom of the logfile"""
        why_sim_ended = "there were no remaining living people." if pop_size == total_dead else "the virus was extinguished."
        with open(self.logfile, "a") as logger:
            logger.writelines([f"\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
            f"The simulation ended after {time_step_number} steps because {why_sim_ended}\n",
            f"Total number of interactions: {number_of_interactions}\n",
            f"Number of times a person was protected by a vaccine: {times_a_vaccination_protected_a_person}"])

        with open(self.logfile, "a") as logger:
            logger.writelines([f"\n\nTotal living: {total_living} \tTotal dead: {total_dead} \tNumber of vaccinations: {number_of_vaccinations}\n",
            f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"])