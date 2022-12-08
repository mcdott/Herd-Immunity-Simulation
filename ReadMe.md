# Final Project: Herd Immunity Simulation

This program simulates how a virus spreads through a partially vaccinated population.

## Usage

This program is written in Python. You can run it from the command line with the following command:

```python
python3 simulation.py
```

followed by the command line arguments in the following order, separated by spaces: {population size} {vacc_percentage} {virus_name} {mortality_rate} {repro_rate} {optional: number of people initially infected (default is 1)}

Here's an example:

- Population Size: 100,000
- Vaccination Percentage: 90%
- Virus Name: Ebola
- Mortality Rate: 70%
- Reproduction Rate: 25%
- People Initially Infected: 10

You can run the example by entering:

```python
python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10
```

in the terminal.
