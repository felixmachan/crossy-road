import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, Lives

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
screen.onkeypress(player.move, "w")
game_is_on = True
cycle = 0
scoreboard = Scoreboard()
lives = Lives()
while game_is_on:
    cycle += 1
    time.sleep(0.1)
    # car_manager.car_move()
    screen.update()
    if cycle % 6 == 0:
        car_manager.create_car()
    car_manager.cars_move()
    for car in car_manager.all_cars:
        if player.distance(car.xcor(), car.ycor(),) < 20:
            lives.deduct_life()
            if lives.lives == 0:
                game_is_on = False
                scoreboard.game_over()
            else:
                player.go_to_start()
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.point()


screen.exitonclick()
