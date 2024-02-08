from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.color(random.choice(COLORS))
        # self.cars = []
        # self.create_car()
        # self.car_move()
        # self.speed(10)
        # self.penup()
        # self.shape("square")
        # self.shapesize(1, 2)
        # self.setheading(180)
        # self.goto(260, random.randint(20, 250))

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        # new_car.setheading(180)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



