class Car:
    def __init__(self, max_speed):
        self.speed = 0
        self.max_speed = max_speed

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

car = Car(150)

car.accelerate(30)
print("Speed after +30 km/h:", car.speed)

car.accelerate(70)
print("Speed after +70 km/h:", car.speed)

car.accelerate(50)
print("Speed after +50 km/h:", car.speed)

car.accelerate(-200)
print("Speed after emergency brake:", car.speed)
