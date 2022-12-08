from logger import Logger
from datetime import date

def test_write_metadata():
    """Tests that the logfile contains the correct metadata content"""
    logger_file = "logfile_test.txt"
    logger = Logger(logger_file)
    logger.write_metadata("Influenza", 0.05, 0.9, 0, 50000, 25)
    file = open(logger_file, "r")
    content = file.readlines()
    assert content == ([f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",
        f"Simulation date: {date.today()}\n\n",
        f"Virus: Influenza \tMortality rate: 0.05 \tReproduction rate: 0.9", 
        f"\nStep 0\t\tPopulation size: 50000\t\tInitial number infected: 25\n",
        f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"])


# if __name__ == "__main__":
#     test_write_metadata()