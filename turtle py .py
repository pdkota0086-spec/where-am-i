import turtle    #importing library
turtle.Screen().bgcolor("red")
turtle.Screen().setup(750,750)
polygon = turtle.Turtle() #defined variable
 
num_sides =8 #variable
side_length = 50
angle = 360.0 / num_sides


#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(20)
    polygon.right(95)
    

import turtle     #importing library       
my_wn = turtle.Screen()
my_wn.bgcolor("green") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0
while True: #iterate loop
  for i in range(4): 
    my_pen.forward(size)
    my_pen.left(25)
    size=size+2

turtle.done()