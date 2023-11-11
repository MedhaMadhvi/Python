# Write a Python program to create a class named Car with attributes model, color and price. Implement methods to start, stop, and accelerate the car. Also, implement a static method to count the number of cars created.
class Car:
    car_count = 0

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        Car.car_count += 1

    def start(self):
        return f"{self.model} is starting."

    def stop(self):
        return f"{self.model} is stopping."

    def accelerate(self):
        return f"{self.model} is accelerating."

    @staticmethod
    def count_cars():
        return f"Total numbers of cars created: {Car.car_count}"

num_car = int(input("Enter the number of car: "))
for i in range(num_car):
    print(f"Enter details of {i+1} car")
    model_name = input(f"Enter model: ")
    color = input(f"Enter colour: ")
    price = float(input(f"Enter price: "))
    car = Car(model_name, color, price)

print(car.start())
print(car.accelerate())
print(car.stop())
print(Car.count_cars())