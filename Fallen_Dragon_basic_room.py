import turtle, time

wn = turtle.Screen()
wn.title("TK by zpie")

wn.bgcolor("white")
wn.setup(width=800, height = 600)

##objects
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("black")
player.penup()
player.goto(-400,-285)

gateway = turtle.Turtle()
gateway.speed(0)
gateway.shape("circle")
gateway.penup()
gateway.color("red")
gateway.goto(0,-20)
gateway.shapesize(stretch_wid=5, stretch_len=5)
gateway.left(90)
gateway.goto(-330,-20)
gateway.color("white")



BouncePad = turtle.Turtle()
BouncePad.speed(0)
BouncePad.shape("square")
BouncePad.color("blue")
BouncePad.penup()
BouncePad.goto(400,0)
#BouncePad.shapesize(stretch_wid=5, stretch_len=10)
onceClear = False

middleblock = turtle.Turtle()
middleblock.speed(0)
middleblock.shape("square")
middleblock.penup()
middleblock.goto(0,0)
middleblock.shapesize(stretch_wid=20, stretch_len=25)


enemy = turtle.Turtle()
enemy.speed(0)
enemy.color("red")
enemy.shape("triangle")
enemy.penup()
enemy.goto(300,-285)
enemy.left(90)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Welcome", align="center",font=("arial",24,"normal"))

coin = turtle.Turtle()
coin.speed(0)
coin.shape("square")
coin.color("yellow")
coin.penup()
coin.goto(350,-100)

playerYEnable = False
def playerup():
    if player.ycor() < 280:
        if playerYEnable:
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
def removeObject(Object):
    Object.color("white")
    Object.setx(1000)
def clearObjects():

    removeObject(player)
    removeObject(BouncePad)
    removeObject(coin)
    removeObject(enemy)
    removeObject(middleblock)


def ending(type):
    if type == ('win'):
        clearObjects()
        gateway.setx(0)
        gateway.sety(0)
        gateway.color("black")
        for x in range(0,5):
            x += 1
            time.sleep(.3)
            gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
    if type == ('loose'):
        clearObjects()
        gateway.setx(0)
        gateway.sety(0)
        gateway.color("red")
        for x in range(0,5):
            x += 1
            time.sleep(.3)
            gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
    time.sleep(5)


wn.listen()
wn.onkeypress(playerup, "w")
wn.onkeypress(playerdown, "s")
wn.onkeypress(playerleft, "a")
wn.onkeypress(playerright, "d")

#wn.onkeypress(paddleBup, "Up")
#wn.onkeypress(paddleBdown, "Down")

def areObjectsTouching(ObjectOne,ObjectTwo, size):
    #print("player:", ObjectOne.xcor(), "coin:", ObjectTwo.xcor())   print objects cordinates
    if ObjectOne.xcor() > ObjectTwo.xcor() - size and ObjectOne.xcor() < ObjectTwo.xcor() + size and ObjectOne.ycor() > ObjectTwo.ycor() - size and ObjectOne.ycor() < ObjectTwo.ycor() + size:
        #print(ObjectOne, " has collided with", ObjectTwo)
        return True
gateway.color("red")
gateway.goto(-330,-20)
while True:
    print(player.xcor(),player.ycor(), enemy.xcor(), enemy.ycor())
    wn.update()
    if player.xcor() > 260:
        playerYEnable = True
        player.color("blue")
        playerYEnable = True
    elif player.xcor() < 260:
        player.color("black")
        playerYEnable = False
        if onceClear == False:
            pen.clear()
        if player.ycor() > 0 and player.xcor() > -240:
            player.sety(215)
        elif player.ycor() > 0 and player.xcor() < -240:
            if player.color() != ("blue"):
                player.color("blue")
        onceClear = True
        if player.ycor() < 0 and player.xcor() > -260 and player.xcor() < 240:
            player.sety(-285)
    elif player.xcor() < -260 and player.ycor > 0:
        player.color("blue")
        playerYEnable = True
        pen.write("you are now in a antigravity zone", align="center",font=("arial",22,"normal"))
    if areObjectsTouching(player,enemy, 20):
        ending('loose')
    if areObjectsTouching(player, gateway, 50):
        ending('win')
        
        
        
