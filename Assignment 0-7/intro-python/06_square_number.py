def main():
    number = float(input("\033[1;3m Enter your number: \033[0m"))
    
    square = number * number
    
    print(f"The square of {number} is {square}.")
    
if __name__ == "__main__":
    main()