class Dog:

    species = 'pet'

    def __init__(self, breed, colour):
        self.animal = "dog"
        self.breed = breed
        self.colour = colour


golden_retriever = Dog(breed="Golden Retriever", colour="golden")
Labrador = Dog(breed="Labrador", colour="brown")


print('golden_retriever is a {}'.format(golden_retriever.species))
print('Labrador is a {}'.format(Labrador.species))

print('{} is {} colour'.format(golden_retriever.breed , golden_retriever.colour))
print('{} is {} colour'.format(Labrador.breed , Labrador.colour))