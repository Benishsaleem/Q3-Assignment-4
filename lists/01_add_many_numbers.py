def sum_of_numbers(numbers):
    total = 0  
    for num in numbers:
        total += num
    return total

def main():
    numbers_list = [1, 2, 3, 4, 5]
    result = sum_of_numbers(numbers_list)
    print(f"list: {numbers_list}")
    print(f"Sum of numbers: {result}")
    
if __name__ == "__main__":
    main()
        