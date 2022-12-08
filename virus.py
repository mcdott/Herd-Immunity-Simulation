class Virus(object):
    """ This class contains the attributes of the virus used in Simulation."""
    def __init__(self, virus_name, mortality_rate, repro_rate):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate    
        self.repro_rate = repro_rate



# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus1 = Virus("HIV", 0.3, 0.8)
    assert virus1.virus_name == "HIV"
    assert virus1.mortality_rate == 0.3
    assert virus1.repro_rate == 0.8

    virus2 = Virus("Ebola", 0.7, 0.25)
    assert virus2.virus_name == "Ebola"
    assert virus2.mortality_rate == 0.7
    assert virus2.repro_rate == 0.25

    virus3 = Virus("Influenza", 0.05, 0.9)
    assert virus3.virus_name == "Influenza"
    assert virus3.mortality_rate == 0.05
    assert virus3.repro_rate == 0.9