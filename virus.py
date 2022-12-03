class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, virus_name, mortality_rate, repro_rate):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate    
        self.repro_rate = repro_rate



# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.3, 0.8)
    assert virus.virus_name == "HIV"
    assert virus.mortality_rate == 0.3
    assert virus.repro_rate == 0.8
