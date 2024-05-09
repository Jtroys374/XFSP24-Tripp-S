
import math
import random as rnd
from datetime import datetime

class Position:
    def __init__(self, pos=None, x=None, y=None, z=None):
        self.x = x if x is not None else 0.0
        self.y = y if y is not None else 0.0
        self.z = z if z is not None else 0.0
        if pos is not None:
            self.x, self.y, self.z = pos

    def __add__(self, other):
        return Position((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        return Position((self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Position((self.x * other, self.y * other, self.z * other))
        return self  # Placeholder for vector multiplication

    def __truediv__(self, other):
        return Position((self.x / other, self.y / other, self.z / other))

    def mag(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def normalize(self):
        l = self.mag()
        if l > 0:
            self.x /= l
            self.y /= l
            self.z /= l

class macroMolecule:
    def __init__(self, meanDegreeOfPolymerization=1000, segmentLength=0.154E-9, merWt=14):
        stddev = 0.1 * meanDegreeOfPolymerization
        self.N = int(rnd.normalvariate(meanDegreeOfPolymerization, stddev))
        self.merWt = merWt
        self.MW = self.N * merWt
        self.segmentLength = segmentLength
        self.centerOfMass = Position()
        self.radiusOfGyration = 0
        self.endToEndDistance = 0
        self.mers = []  # List of positions

    def freelyJointedChainModel(self):
        # Placeholder for chain model simulation
        pass

# Placeholder for further methods and simulation details

import random as rnd
import numpy as np

# Importing the necessary classes from a module (assuming import from modified polymer file)
# from polymer_module import Position, macroMolecule

# Placeholder definitions for Position and macroMolecule, assuming they are imported
class Position:
    def __init__(self, pos=None, x=None, y=None, z=None):
        self.x = x if x is not None else 0.0
        self.y = y if y is not None else 0.0
        self.z = z if z is not None else 0.0
        if pos is not None:
            self.x, self.y, self.z = pos

    def __add__(self, other):
        return Position((self.x + other.x, self.y + other.y, self.z + other.z))

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Position((self.x * other, self.y * other, self.z * other))
        return self

class macroMolecule:
    def __init__(self, meanDegreeOfPolymerization=1000, segmentLength=0.154E-9, merWt=14):
        stddev = 0.1 * meanDegreeOfPolymerization
        self.N = int(rnd.normalvariate(meanDegreeOfPolymerization, stddev))
        self.merWt = merWt
        self.MW = self.N * merWt
        self.segmentLength = segmentLength
        self.centerOfMass = Position()
        self.radiusOfGyration = 0
        self.endToEndDistance = 0

    def freelyJointedChainModel(self):
        # Simplified model for the freely jointed chain simulation
        self.centerOfMass = Position((rnd.random(), rnd.random(), rnd.random()))  # Placeholder
        self.radiusOfGyration = rnd.random()  # Placeholder
        self.endToEndDistance = rnd.random()  # Placeholder

def main():
    # Input from user
    N = int(input("degree of polymerization (1000)?: "))
    num_molecules = int(input("How many molecules (50)?: "))
    
    # Create molecules and perform simulation
    molecules = [macroMolecule(meanDegreeOfPolymerization=N) for _ in range(num_molecules)]
    for molecule in molecules:
        molecule.freelyJointedChainModel()
    
    # Calculate metrics
    centers_of_mass = [mol.centerOfMass for mol in molecules]
    total_x = sum(pos.x for pos in centers_of_mass) / num_molecules
    total_y = sum(pos.y for pos in centers_of_mass) / num_molecules
    total_z = sum(pos.z for pos in centers_of_mass) / num_molecules
    avg_center_of_mass = Position(x=total_x, y=total_y, z=total_z)

    radii_of_gyration = [mol.radiusOfGyration for mol in molecules]
    end_to_end_distances = [mol.endToEndDistance for mol in molecules]
    molecular_weights = [mol.MW for mol in molecules]

    # Compute averages and standard deviations
    avg_radius_of_gyration = np.mean(radii_of_gyration)
    std_radius_of_gyration = np.std(radii_of_gyration)
    avg_end_to_end_distance = np.mean(end_to_end_distances)
    std_end_to_end_distance = np.std(end_to_end_distances)
    pdi = np.std(molecular_weights) ** 2 / np.mean(molecular_weights)

    # Output results
    print(f"Metrics for {num_molecules} molecules of degree of polymerization = {N}")
    print(f"Avg. Center of Mass (nm) = {avg_center_of_mass.x:.3f}, {avg_center_of_mass.y:.3f}, {avg_center_of_mass.z:.3f}")
    print("End-to-end distance (μm):")
    print(f"\tAverage = {avg_end_to_end_distance:.3f}")
    print(f"\tStd. Dev. = {std_end_to_end_distance:.3f}")
    print("Radius of gyration (μm):")
    print(f"\tAverage = {avg_radius_of_gyration:.3f}")
    print(f"\tStd. Dev. = {std_radius_of_gyration:.3f}")
    print(f"PDI = {pdi:.2f}")

if __name__ == "__main__":
    main()
