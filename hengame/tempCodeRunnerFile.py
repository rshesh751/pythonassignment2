        if hen.ycor() <= -240:
            hen.goto(0,330)
            speed-=0.2
            level+=1
            score.clear()
            score.write(f"level : {level}",align="center",font=("Arial","24","normal"))
            continue
    screen.update()
