class Reverse:
    def __init__(self, s=""):
        self.s = s  

    def reverse_string(self):
        return self.s[::-1]  


input_string = input("Enter a string: ")


reverser = Reverse(input_string)


print("Reversed string:", reverser.reverse_string())