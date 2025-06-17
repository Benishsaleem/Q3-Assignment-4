import math

def main():
    
    #lenghths of two sides of a right angled triangle ABC
    
    ab = float(input(" \033[1;3m Enter length of AB: \033[0m"))
    ac = float(input(" \033[1;3m Enter length of AC: \033[0m"))
    
    #Hypotenous BC
    
    bc = float(math.sqrt(ab**2 + ac**2))
    
    print(f"The length of BC is {bc}.")
    
if __name__ == "__main__":
    main()