from turtle import Turtle

POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for p in POS:
            self.add_segment(p)

    def add_segment(self, position):
        new_sqr = Turtle(shape="square")
        new_sqr.color("white")
        new_sqr.penup()
        new_sqr.goto(position)
        self.segments.append(new_sqr)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(new_x, new_y)
        self.head.forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
