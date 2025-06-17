import random

NUM_SIDES = 6

def main():
    die1:int = random.randint(1, NUM_SIDES)
    die2:int = random.randint(1, NUM_SIDES)
    
    total:int = die1 + die2
    
    print(f"Dice have {NUM_SIDES} sides each")
    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"Total of two Dice: {total}")
    
    
if __name__ == "__main__":
    main()