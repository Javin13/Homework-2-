import pgzrun

width = 400
height = 400
car = Actor('car_red',center=(200,300))
def draw():
    screen.clear()
    car.draw()

draw()