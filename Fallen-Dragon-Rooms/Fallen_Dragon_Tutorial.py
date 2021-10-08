import turtle, time
from os import path
import os
wn = turtle.Screen()
wn.title("Fallen Dragon by zpie")
#wn.addshape('mario.gif')
wn.bgcolor("white")
wn.setup(width=800, height = 600)

wn.addshape('BlueGuy.gif')
wn.addshape('blackGuy.gif')
os.system('clear')
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#intro = False
story = False
if True:
# intro
    pen.write("Welcome To the relm of the fallen dragon", align="center",font=("Comic Sans",24,"normal"))
    if story:

        time.sleep(3)
        pen.clear()
        pen.write("Legend has it that thousands of years ago there was a mighty dragon", align="center",font=("Comic Sans",12,"normal"))
        time.sleep(5)
        pen.clear()
        pen.write("he held power over all of the lands", align="center",font=("Comic Sans",15,"normal"))
        time.sleep(3)
        pen.clear()
        pen.write("as the legend says, his inheritance was given to his great grandson who is was the current king, untill last night", align="center",font=("Comic Sans",10,"normal"))
        time.sleep(5)
        pen.clear()
        pen.write("he died last night and you are here for his gold", align="center",font=("Comic Sans",24,"normal"))
    time.sleep(4)
    pen.clear()
    pen.write("you are a very good bandit,and you are planning on sneaking in to the castle tonight, so we need to get you ready", align="center",font=("Comic Sans",10,"normal"))
    time.sleep(4)
    pen.clear()
    pen.write("the castle consists of square rooms, the goal is to get to the gateway, witch leads to the next room", align="center",font=("Comic Sans",12,"normal"))
    time.sleep(4)
    pen.clear()
    pen.write("the gateway is uselly near the beginning of the room, but cannot be reached from the beggining", align="center",font=("Comic Sans",12,"normal"))
    wn.addshape('hole.gif')
    wn.addshape('coin.gif')
    gateway = turtle.Turtle()
    #gateway.speed(0)
    gateway.shape('hole.gif')
    gateway.penup()
    #gateway.color("red")


    gateway.goto(0,-20)
    gateway.shapesize(stretch_wid=5, stretch_len=5)
    gateway.left(90)
    time.sleep(4)
    gateway.goto(-330,-20)
    gateway.setx(1000)
    pen.clear()
    player = turtle.Turtle()
    player.speed(0)
    #player.shape("mario.gif")   # make player look like mario
    #turtle.setup(500,500)
    player.shape("square")
    #player.shapesize(stretch_len=-10 , stretch_wid=-10)
    #player.turtlesize(stretch_len=-10, stretch_wid=-10)
    player.shape('blackGuy.gif')
    #wn.addshape('mario40x80.gif')
    player.penup()
    player.goto(0,0)
    #time.sleep(4)
    pen.clear()
    pen.write("when your player is black you can move horizontaly", align="center",font=("Comic Sans",15,"normal"))
    for p in range (0,10):
        p += 1
        time.sleep(.1)
        wn.update()
        player.setx(player.xcor() + 20)
    for p in range (0,10):
        p += 1
        time.sleep(.1)
        wn.update()
        player.setx(player.xcor() - 20)
    time.sleep(1)
    ##objects
    pen.clear()
    pen.write("when your player is blue you can move verticaly", align="center",font=("Comic Sans",15,"normal"))
    player.shape('BlueGuy.gif')
    for p in range (0,10):
        p += 1
        time.sleep(.1)
        wn.update()
        player.sety(player.ycor() + 20)
    for p in range (0,10):
        p += 1
        time.sleep(.1)
        wn.update()
        player.sety(player.ycor() - 20)
    time.sleep(1)
    #time.sleep(3)
    pen.clear()
    pen.write("Your player starts in the bottom left", align="left",font=("Comic Sans",15,"normal"))



# /intro


player.shape('blackGuy.gif')
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
coin.shape('coin.gif')
#coin.color("yellow")
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
roomDone = False # is the room done yet, used for ending animation
gateway.goto(-330,-20) # bring it back into view
while True: # game loop
    print("points:  ", points)


    if roomDone == False:
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
                if roomDone == False:
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
            print("player collided with BP")
        #if areObjectsTouching(player, wall, ):
            #print("player is in blue box")
            player.sety(player.ycor() + 200)

            #pen.clear()
            #for x in range (0,10):
            #   time.sleep(.5)
            #  wn.update()
        if mapOriantation == 'right':
            print("MapOriantation = right")
            playerJump = False
            player.shape('blackGuy.gif')
        if mapOriantation == 'upRight':
            print("mapOriantaion = upRight")
            playerJump = True
            player.shape('BlueGuy.gif')
        if areObjectsTouching(player, gateway, 50):
            print("Player collided with Gatway")
            roomDone = True
            pen.clear()
            removeObject(player)
            removeObject(wall)
            removeObject(coin)
            removeObject(arrow)
            removeObject(arrow2)
            gateway.setx(0)
            gateway.sety(0)
            gateway.shape("circle")
            gateway.color("red")
            for x in range(0,5):
                x += 1
                time.sleep(.3)
                gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
            pen.write("Tutorial Room complete", align="center", font=("Comic Sans",24,"normal"))
            time.sleep(10)        
    
            wn.bye()
            os.system('python3 Fallen-Dragon/Fallen-Dragon-Rooms/Fallen_Dragon_Room_One.py')
            
        if player.xcor() > 100 and player.ycor() > 100:
            playerYEnable = True
            player.shape('BlueGuy.gif')
            playerYEnable = True
        elif player.xcor() < 100 and player.ycor() > 0:# if top left
            print("player x < 100 and y is positive")
            player.shape('blackGuy.gif')
            mapOriantation = ('right')
            playerYEnable = False
            if player.ycor() > 0 and player.xcor() > -100: # if top middle
                print("player y positive and x > -100")
                player.sety(110)
            elif player.ycor() > 0 and player.xcor() < -100:
                if player.color() != ("blue"):
                    player.shape('BlueGuy.gif')
            onceClear = True
        if player.ycor() < 0 and player.xcor() > -100 and player.xcor() < 100:  # if the player is on the botom level and in the middle
                player.sety(-285)
        elif player.xcor() < -100 and player.ycor() > 0:
            player.shape('BlueGuy.gif')
            mapOriantation = ('upRight')
            playerYEnable = True
            #pen.write("you are now in a antigravity zone", align="center",font=("arial",22,"normal"))

            