from turtle import Turtle,Screen
import random
import time
def down():
    hen.setheading(270)
    hen.forward(20)
def cars():
    l=[]
    for i in range(100):
        k=random.randint(0,2)
        m=[]
        x=-300-(i*100)
        for j in range(k):
            car=Turtle()
            car.penup()
            car.shape(random.choice(colos))
            car.shapesize(5,5)
            car.goto(x,random.choice(pos))
            m+=[car]
        l+=[m]
    screen.update()
    return l
hen=Turtle()
hen.shape("circle")
hen.color("black")
hen.setheading(90)
hen.penup()
screen=Screen()
screen.register_shape("hen1 (1).gif")
screen.register_shape("download2.gif")
screen.register_shape("download3.gif")
screen.register_shape("download4.gif")
screen.setup(600,800)
screen.tracer(0)
screen.bgpic("background2 (1).gif")
hen.shape("hen1 (1).gif")
hen.goto(0,330)
screen.listen()
screen.onkey(down,"Down")
pos=[180,60,-60,-180]
colos=["download2.gif","download3.gif","download4.gif"]
#score_board
score=Turtle()
score.penup()
score.goto(0,350)
score.write("Level : 1",align="center",font=("Arial","24","normal"))
level = 1
speed=1
game_on=True
l=cars()
while game_on:
    for i in range(100):
        for k in l[i]:
            k.forward(100)
            if k.xcor()==0:
                if hen.distance(k) <= 40:
                    game_on=False
                    break
            if game_on==False:
                break
        screen.update()
        if hen.ycor() <= -240:
            hen.goto(0,330)
            speed-=0.2
            level+=1
            score.clear()
            score.write(f"level : {level}",align="center",font=("Arial","24","normal"))
            continue
    screen.update()
    time.sleep(speed)
screen.clear()
score.goto(0,0)
score.write(f"GAME OVER \n score : {level}",align="center",font=("Arial","50","normal"))

with open("Highscore.txt","r") as h_file:
    high_score=h_file.read()
if level > int(high_score):
    with open("Highscore.txt","w") as h_file2:
        h_file2.write(str(level))
screen.update()
screen.exitonclick()                                                    
