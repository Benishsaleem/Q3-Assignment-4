C = 299792458  # Speed of light in m/s

def main():
    mass_in_kg = float(input("\033[1;3m Enter Kilos of Mass: \033[0m"))
    
    energy_in_joules = mass_in_kg * (C**2)
    
    print("e = m * C^2")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")
    
if __name__ == "__main__":
    main()