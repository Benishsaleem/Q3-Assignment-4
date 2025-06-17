def main():
    dividend:int = int(input("\033[1;3m Enter a number to be divided \033[0m"))
    divisor:int = int(input("\033[1;3m Enter a number to divide by \033[0m"))
    
    quotient:int = dividend // divisor  #answer without reminder
    remainder:int = dividend % divisor #give remainder
    
    print(f"The result of this division is {quotient} with a remainder {remainder}")
    
if __name__ == "__main__":
    main()