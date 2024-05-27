from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()

    def create_car(self):
        """creates a car randomly with 20% chance for each clock cycle"""
        if random.randint(1, 5) >= 5:
            start_y = random.randint(-240, 240)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(x=310, y=start_y)
            self.cars.append(new_car)

    def move_cars(self):
        """moves all cars to left on each clock cycle"""
        for car in self.cars:
            current_x = car.xcor()
            current_y = car.ycor()
            car.goto(current_x-STARTING_MOVE_DISTANCE, current_y)

    def reset_cars(self):
        """clears car graphics and cars list object"""
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

