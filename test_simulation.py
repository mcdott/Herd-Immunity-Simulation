from simulation import Simulation
from virus import Virus

def test_simulation():
    """Tests that a virus object is instatiated correctly from Virus"""
    virus = Virus("HIV", 0.3, 0.8)
    simulation = Simulation(100000, 0, virus, 5)
    assert simulation.pop_size == 100000
    assert simulation.vacc_percentage == 0
    assert simulation.virus == virus
    assert simulation.initial_infected == 5

# if __name__ == "__main__":
#     test_simulation()