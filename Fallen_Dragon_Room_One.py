import turtle, time, os, sys, json
#from Fallen_Dragon_Tutorial import points
#points = int(sys.argv[1])
#print(sys.argv[1])

with open('data.json', 'r') as openfile:
  
    # Reading from json file
    json_object = json.load(openfile)
  
print(json_object)


points = (int(json_object))
wn = turtle.Screen()
wn.title("TK by zpie")

wn.bgcolor("white")
wn.setup(width=800, height = 600)
wn.addshape('BlueGuy.gif')
wn.addshape('blackGuy.gif')

wn.addshape('hole.gif')
wn.addshape('coin.gif')

wn.addshape('mine.gif')

##objects
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.shape('blackGuy.gif')
player.penup()
player.goto(-400,-285)
#player.shape('mario40x80.gif')
gateway = turtle.Turtle()
#gateway.speed(0)
gateway.shape('hole.gif')
gateway.penup()
gateway.color("red")
gateway.goto(0,-20)
#gateway.shapesize(stretch_wid=100, stretch_len=100)
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

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
#pen.write("Welcome", align="center",font=("arial",24,"normal"))

pen.write("Room One", align="center", font=("Comic Sans",24,"normal"))

enemy = turtle.Turtle()
#enemy.speed(0)
enemy.color("red")
enemy.shape('mine.gif')
enemy.penup()
enemy.goto(300,-285)
enemy.left(90)

enemy2 = turtle.Turtle()
#enemy2.speed(0)
enemy2.color("red")
enemy2.shape('mine.gif')
enemy2.penup()
enemy2.goto(250,-250)
enemy2.left(90)

enemy3 = turtle.Turtle()
#enemy3.speed(0)
enemy3.color("red")
enemy3.shape('mine.gif')
enemy3.penup()
enemy3.goto(250,250)
enemy3.left(90)


#points = 0

coin = turtle.Turtle()
coin.speed(0)
coin.shape('coin.gif')
#coin.color("yellow")
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

coin1Grabed = False

def clearObjects():

    removeObject(player)
    removeObject(BouncePad)
    removeObject(coin)
    removeObject(enemy)
    removeObject(middleblock)
    removeObject(enemy3)
    removeObject(enemy2)

roomDone = False
def ending(type):
    roomDone = True
    gateway.shape("circle")
    if type == ('win'):
        clearObjects()
        gateway.setx(0)
        gateway.sety(0)
        gateway.color("red")
        for x in range(0,5):
            x += 1
            time.sleep(.3)
            gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
        print("here")
        wn.bye()
        os.system('python3 Fallen-Dragon-Rooms/Fallen_Dragon_Room_One.py')
    if type == ('loose'):
        clearObjects()
        gateway.setx(0)
        gateway.sety(0)
        gateway.color("black")
        pen.color("red")
        pen.write("You Died", align="center", font=("Comic Sans",24,"normal"))
        

        for x in range(0,5):
            x += 1
            time.sleep(.3)
            gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
    time.sleep(5)



#time.sleep(4)
pen.clear()
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
      if roomDone == False:
        print(player.xcor(), player.ycor(), "points:", points)
        wn.update()
        if enemy3.xcor() < 300:
            enemy3.setx(enemy3.xcor() + 5)
            #time.sleep(1)
            #time.sleep(.1)
        if enemy3.xcor() > 100:
            enemy3.setx(enemy3.xcor() - 5)
            #time.sleep(1)
            #time.sleep(.1)
        if player.xcor() > 260:
            playerYEnable = True
            player.shape('BlueGuy.gif')
            playerYEnable = True
        elif player.xcor() < 260:
            player.shape('blackGuy.gif')
            playerYEnable = False
            if onceClear == False:
                pen.clear()
            if player.ycor() > 0 and player.xcor() > -240:
                player.sety(215)
            elif player.ycor() > 0 and player.xcor() < -240:
                if player.color() != ("blue"):
                    player.shape('BlueGuy.gif')
            onceClear = True
            if player.ycor() < 0 and player.xcor() > -260 and player.xcor() < 240:
                player.sety(-285)
        elif player.xcor() < -260 and player.ycor > 0:
            player.shape('BlueGuy.gif')
            playerYEnable = True
            pen.write("you are now in a antigravity zone", align="center",font=("arial",22,"normal"))
        if areObjectsTouching(player,enemy, 20) or areObjectsTouching(player, enemy3, 20) or areObjectsTouching(player, enemy2, 20):
            ending('loose')
        if areObjectsTouching(player, gateway, 50):
            clearObjects()
            gateway.setx(0)
            gateway.sety(0)
            gateway.color("red")
            for x in range(0,5):
                x += 1
                print(x)
                time.sleep(.3)
                gateway.shapesize(stretch_wid=10 * x, stretch_len=10 * x)
            #print("here")
            wn.bye()


            with open("data.json", "w") as outfile:
                json.dump(points, outfile)

            os.system('python3 Fallen_Dragon_Room_Two.py')
 
            #os.system('python3 Fallen-Dragon-Rooms/Fallen_Dragon_Room_One.py')
        if areObjectsTouching(player, coin, 20):
                if coin1Grabed == False:
                    points += 1
                    coin1Grabed = True
                    removeObject(coin)
                    pen.clear()
                    #pen.write("coin collected", align="center", font=("Comic Sans",12,"normal"))
                    time.sleep(.5)
                    pen.clear()
        pen.write(points, align="center", font=("Comic Sans",12,"normal"))
            
            
