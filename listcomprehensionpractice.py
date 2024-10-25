
#Activity 1


def create_odd_lists():
    
    user_input = int(input("Enter a number: "))

    
    odd_numbers = [num for num in range(user_input) if num % 2 != 0]

   
    other_odd_numbers = [num for num in range(1, 20, 2)]

    print("Odd numbers under {}: {}".format(user_input, odd_numbers))
    print("Other odd numbers: {}".format(other_odd_numbers))

create_odd_lists()


#Activity 2

def capitalize_fruits():
    # List of fruits
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    # Create a new list with the first letter capitalized
    capitalized_fruits = [fruit.capitalize() for fruit in fruits]

    print("Original list:", fruits)
    print("Capitalized list:", capitalized_fruits)

capitalize_fruits()
