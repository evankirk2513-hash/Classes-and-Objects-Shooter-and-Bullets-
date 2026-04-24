from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.player_color = color
        self.pencolor(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.colors = [color,"red","yellow"]
        self.health = 3
        self.alive = True
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def fire(self):
        self.bullets.append(Bullet(self))
    
    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())
    
    def damage(self):
        self.health -= 1
        if self.health > 0:
            self.pencolor(self.colors[self.health])
        else:
            self.ht()
            self.alive = False


class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(player.player_color)
        self.penup()
        self.setheading(player.heading()) 
        self.goto(player.xcor(),player.ycor())
        self.forward(10)
        self.player = player
        self.st()
    
    def move(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.remove()
        if self.ycor() > 230 or self.ycor() < -230:
            self.remove()
    
    def remove(self):
        if self in self.player.bullets:
            self.ht()
            self.player.bullets.remove(self)



screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a", "w")
p2 = Player(100,0,"blue",screen, "Right","Left", "Up")

while p1.alive and p2.alive:
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move()
        if p2.distance(bullet) <= 10:
            p2.damage()
            bullet.remove()
    for bullet in p2.bullets:
        bullet.move()
        if p1.distance(bullet) <= 10:
            p1.damage()
            bullet.remove()


screen.exitonclick()