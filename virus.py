class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, virus_name, repro_rate, mortality_rate):
        self.virus_name = virus_name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate    
        # TODO Define the other attributes of Virus
        pass


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.virus_name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
