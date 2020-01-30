# access the code in the turtle module
import turtle
import random
from tkinter import messagebox


class RaceTrack:
    def setupTrack(self):
        raceTrack.bgcolor('lightgreen')


class TurtleRacer:
    def __init__(self,color1,color2,color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def configureTurtles(self):
        larry.hideturtle()
        larry.shape('turtle')
        larry.color(self.color1)
        larry.shapesize(3)
        larry.up()

        curly.hideturtle()
        curly.shape('turtle')
        curly.color(self.color2)
        curly.shapesize(3)
        curly.up()

        moe.hideturtle()
        moe.shape('turtle')
        moe.color(self.color3)
        moe.shapesize(3)
        moe.up()


class RaceProgram:
    def lineupTurtlesForRace(self):
        # point larry upwards to get it ready for the race
        larry.left(90)

        # point curly left of larry by 200 pixels
        curly.left(180)
        curly.forward(200)
        curly.right(90)

        # point moe right of larry by 200 pixels
        moe.forward(200)
        moe.left(90)

        # the turtles are read to race so show them
        larry.showturtle()
        larry.down()
        curly.showturtle()
        curly.down()
        moe.showturtle()
        moe.down()

    def startRace(self):
        # start the race. Generate 3 random distances for the 3 turtles to travel

        racing = True
        while racing:
            distance = random.randint(2, 100)

            # check if larry is going to cross the finish line. How?
            # if larry's y-coordinate plust the distance to travel is greater
            # than half of the window height
            if larry.ycor() + distance >= raceTrack.window_height() / 2 - turtleShapeHeight / 2:
                # larry has reached the finish line
                larry.forward(raceTrack.window_height() / 2 - turtleShapeHeight / 2 - larry.ycor())

                # larry won
                racing = False
                messagebox.showinfo('Turtle Race', 'Larry won the race.')
            else:
                # larry has not reached not finish line and must keep going
                larry.forward(distance)

            distance = random.randint(2, 100)
            # check if curly is going to cross the finish line. How?
            # if curly's y-coordinate plust the distance to travel is greater
            # than half of the window height
            if curly.ycor() + distance >= raceTrack.window_height() / 2 - turtleShapeHeight / 2:
                # curly has reached the finish line
                curly.forward(raceTrack.window_height() / 2 - turtleShapeHeight / 2 - curly.ycor())

                # curly won
                racing = False
                messagebox.showinfo('Turtle Race', 'Curly won the race.')
            else:
                # curly has not reached not finish line and must keep going
                curly.forward(distance)

            distance = random.randint(2, 100)
            # check if Moe is going to cross the finish line. How?
            # if moe's y-coordinate plust the distance to travel is greater
            # than half of the window height
            if moe.ycor() + distance >= raceTrack.window_height() / 2 - turtleShapeHeight / 2:
                # moe has reached the finish line
                moe.forward(raceTrack.window_height() / 2 - turtleShapeHeight / 2 - moe.ycor())

                # moe won
                racing = False
                messagebox.showinfo('Turtle Race', 'Moe won the race.')
            else:
                # moe has not reached not finish line and must keep going
                moe.forward(distance)

    def determineWinner(self):
        # if larry's y coordinate is higher than curly's
        if larry.ycor() > curly.ycor() and larry.ycor() > moe.ycor():
            print('Larry won the race')

        if curly.ycor() > larry.ycor() and curly.ycor() > moe.ycor():
            print('Curly won the race')

        if moe.ycor() > larry.ycor() and moe.ycor() > curly.ycor():
            print('Moe won the race')


# create and display the window where the race takes place
raceTrack = turtle.Screen()
turtleShapeHeight = 100

# create a turtle named larry, curly and moe and set its color and shape
larry = turtle.Turtle()
curly = turtle.Turtle()
moe = turtle.Turtle()

# setup and start the race
#setupTrack()
#configureTurtles()
#lineupTurtlesForRace()
RaceTrack().setupTrack()
TurtleRacer("blue","black","red").configureTurtles()
RaceProgram().lineupTurtlesForRace()


# ask the turtles if they are ready to race
userAnswer = messagebox.askquestion('Turtle Race', 'Are you ready to race')
# if the user said yes, start the race
if userAnswer == 'yes':
    RaceProgram().startRace()


# tell the window to close itself when clicked
# raceTrack.exitonclick()