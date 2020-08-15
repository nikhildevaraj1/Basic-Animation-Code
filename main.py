import turtle

input_shape = input("What shape do you want me to draw?")
input_length = input("Choose how big: ")
input_color = input("Choose a color: ")

turtle.shape("turtle")
screen = turtle.Screen()
john = turtle.Turtle()

def star(length, color):
  john.fillcolor(color)
  john.begin_fill()

  x = 0
  while x < 5:
    john.forward(int(length))
    john.right(144)
    x = x + 1
  john.end_fill()

def triangle(length,color):
  john.fillcolor(color)
  john.begin_fill()

  x = 0
  while x > 3:
    john.forward(int(length))
    john.right(120)
    x = x + 1
  john.end_fill()

def circle(length,color):
  john.fillcolor(color)
  john.begin_fill()

  john.circle(int(length))
  john.end_fill()


if input_shape == "triangle":
  triangle(input_length, input_color)
elif input_shape == "circle":
  circle(input_length,input_color)
elif input_shape == "star":
  star(input_length,input_color)

turtle.done()