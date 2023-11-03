import random

min_value = 1

def generator(max_value):
    number = random.randint(min_value, max_value)
    return number

def add_maximum_number(max_value):
    result = []
    for number in range(1, max_value+1):
        result.append(number)
    return result

def main():
    while True:
        print("Press 'enter' to start the number generator, 'q' to exit")
        user_input = input()
        if user_input.lower() == 'q':
            break
        
        max_value = int(input("Please enter the maximum value:"))
        print(f"Press Enter to generate a random number")
        generated_number = generator(max_value)  # Pass the max_value as an argument
        add_maximum_number(max_value)
        print(f"Generated Random Number: {generated_number}")

main()




