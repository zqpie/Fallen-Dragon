import turtle, time
from os import path
import os
wn = turtle.Screen()
wn.title("TKgame by zpie")
wn.addshape('mario.gif')
wn.bgcolor("white")
wn.setup(width=800, height = 600)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

intro = True
if intro:
# intro
    pen.write("Welcome To TKland", align="center",font=("Comic Sans",24,"normal"))
    time.sleep(3)
    pen.clear()
    pen.write("Tkland consists of square maps, the goal is to get to the gateway", align="center",font=("Comic Sans",14,"normal"))
    time.sleep(4)
    pen.clear()
    pen.write("the gateway is uselly near the beginning of the level, but cannot be reached from the beggining", align="center",font=("Comic Sans",12,"normal"))

    gateway = turtle.Turtle()
    gateway.speed(0)
    gateway.shape("circle")
    gateway.penup()
    gateway.color("red")
    gateway.goto(0,-20)
    gateway.shapesize(stretch_wid=5, stretch_len=5)
    gateway.left(90)
    time.sleep(4)
    gateway.goto(-330,-20)
    gateway.color("white")
    pen.clear()
    pen.write("when your player is black you can move horizontaly", align="center",font=("Comic Sans",15,"normal"))
    ##objects
    player = turtle.Turtle()
    player.speed(0)
    #player.shape("mario.gif")   # make player look like mario
    #turtle.setup(500,500)
    player.shape("square")
    #player.shapesize(stretch_len=-10 , stretch_wid=-10)
    #player.turtlesize(stretch_len=-10, stretch_wid=-10)
    player.color("black")
    player.penup()
    player.goto(0,0)
    time.sleep(4)
    pen.clear()
    pen.write("when your player is blue you can move verticaly", align="center",font=("Comic Sans",15,"normal"))
    player.color("blue")
    time.sleep(3)
    pen.clear()
    pen.write("Your player starts in the bottom left", align="left",font=("Comic Sans",15,"normal"))



# /intro


player.color("black")
player.goto(-400,-285)


wall = turtle.Turtle()
wall.speed(0)
wall.shape("square")
wall.color("blue")
wall.penup()
wall.goto(200,-200)
wall.shapesize(stretch_wid=5, stretch_len=10)

coin = turtle.Turtle()
coin.speed(0)
coin.shape("square")
coin.color("yellow")
coin.penup()
coin.goto(350,-100)
#coin.shapesize(stretch_wid=5, stretch_len=1)

coin1Grabed = False

ScreenWasCleared = False

#turtle.Turtle().shape('mario.gif')

arrow = turtle.Turtle()
arrow.speed(0)
arrow.shape("square")
arrow.penup()
arrow.goto(0,0)
arrow.shapesize(stretch_wid=10, stretch_len=10)

playerMoveEnable = True  # is the player able to move

arrow2 = turtle.Turtle()
arrow2.speed(0)
arrow2.shape("triangle")
arrow2.penup()
arrow2.goto(200,-200)
arrow2.left(90)


def areObjectsTouching(ObjectOne,ObjectTwo, size):
    #print("player:", ObjectOne.xcor(), "coin:", ObjectTwo.xcor())   print objects cordinates
    if ObjectOne.xcor() > ObjectTwo.xcor() - size and ObjectOne.xcor() < ObjectTwo.xcor() + size and ObjectOne.ycor() > ObjectTwo.ycor() - size and ObjectOne.ycor() < ObjectTwo.ycor() + size:
        #print(ObjectOne, " has collided with", ObjectTwo)
        return True

mapOriantation = 'right'


playerJump = False
def playerup():
    if player.ycor() < 280:
        if playerJump:
            y = player.ycor()
            y += 20
            player.sety(y)
    
def playerleft ():
    if player.xcor() > -400:
        x = player.xcor()
        x -= 20
        player.setx(x)
def playerright ():
    if player.xcor() < 400:
        x = player.xcor()
        x += 20
        player.setx(x)
def playerdown ():
    if player.ycor() > -280:
        y = player.ycor()
        y -= 20
        player.sety(y)
#def playerup():
 #   y = player.ycor()
  #  y += 20
   # player.sety(y)
#def playerdown ():
#    y = player.ycor()
 #   y -= 20
  #  player.sety(y)

wn.listen()
wn.onkeypress(playerup, "w")
wn.onkeypress(playerdown, "s")
wn.onkeypress(playerleft, "a")
wn.onkeypress(playerright, "d")

def isPlayerInBlueBox():
    if player.xcor()>=100 and player.xcor() <= 300 and player.ycor() <= -145 and player.ycor() >= -245:
        return True
def removeObject(Object):
    Object.color("white")
    Object.setx(1000)
#wn.onkeypress(paddleBup, "Up")
#wn.onkeypress(paddleBdown, "Down")
points = 0  # player points
bpmsgRead = False  # was the bounce pad measage read
levelDone = False # is the level done yet, used for ending animation
gateway.color("red")
while True: # game loop



    wn.update()
    #print(wn.setup)
    #pen.clear()
    #print(points)
    #pen.write("Points =",points, align="left",font=("Comic Sans",22,"normal"))


    if player.xcor() > 100 and player.xcor() < 230: # are we in the walk-up zone
        mapOriantation = 'upRight'
        
        if ScreenWasCleared==False:
            pen.clear()
        ScreenWasCleared = True
        if bpmsgRead == False:
            pen.write("these blue boxes are bounce pads", align="center",font=("Comic Sans",22,"normal"))
        bpmsgRead = True
        #pen.write("when your player is blue that means that they can walk forward", align="center", font=("Comic Sans",22,"normal"))
    



    if player.xcor() > 230 and player.xcor() < 260:
        ScreenWasCleared = False
    if player.xcor() >280 and player.ycor() > -250:
        if ScreenWasCleared == False:
            pen.clear()
        ScreenWasCleared = True
        if coin1Grabed == False:
            if levelDone == False:
                pen.write("Collect these coins", align="center",font=("Comic Sans",22,"normal"))
  #  if player.xcor() == coin.xcor:
   #     print("pointgivin")
    if areObjectsTouching(player, coin, 20):
        if coin1Grabed == False:
            points += 1
            coin1Grabed = True
            removeObject(coin)
            pen.clear()
            pen.write("Great, you can use these later in the store", align="center", font=("Comic Sans",12,"normal"))
    print(player.xcor(), player.ycor())   # print players coordinants
    if isPlayerInBlueBox():
        #print("player is in blue box")
        player.sety(player.ycor() + 50)

        #pen.clear()
        #for x in range (0,10):
         #   time.sleep(.5)
          #  wn.update()
    if mapOriantation == 'right':
        playerJump = False
        player.color("black")
    if mapOriantation == 'upRight':
        playerJump = True
        player.color("blue")
    if areObjectsTouching(player, gateway, 50):
        levelDone = True
        pen.clear()
        removeObject(player)
        removeObject(wall)
        removeObject(coin)
        removeObject(arrow)
        removeObject(arrow2)
        gateway.setx(0)
        gateway.sety(0)
        for x in range(0,5):
            x += 1
            time.sleep(.3)
            gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
        pen.write("Level One complete", align="center", font=("Comic Sans",24,"normal"))
        time.sleep(10)

        