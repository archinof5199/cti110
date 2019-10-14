# CTI-110
# P4T1a - Turtle Graphics: Repeating Square
# Francesco Archino
# 10/14/2019
# This program uses Turtle Graphics program
# with nested loops to draw 100 circles

import turtle

turtle.right(180)

turtle.speed(0)

length = 505

for times in range (100):
  for endtimes in range (4):
    turtle.forward(length)
    turtle.right(90)
  length -= 5
  
