class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "350 km/h"


def display_car_info(car):
    print("Fuel Type:" , car.fuel_type())
    print("Max Speed:" ,car.max_speed())


bmw_car = BMW()
ferrari_car = Ferrari()


print("BMW Details:")
display_car_info(bmw_car)
print("Ferrari Details:")
display_car_info(ferrari_car)
