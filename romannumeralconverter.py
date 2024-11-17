class RomanConverter:
    def __init__(self):
        
        self.ROMAN_NUMERALS = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }

    def get_roman_value(self, num):
  
        if num in self.ROMAN_NUMERALS:
            return self.ROMAN_NUMERALS[num]
        else:
            return "Key not found in the dictionary."



converter = RomanConverter()


try:
    key = int(input("Enter a key: "))  
 
    print("Value:", converter.get_roman_value(key))
except ValueError:
    print("Invalid input! Please enter a number.")
