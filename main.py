import turtle
from random import randint

def apply_rules(axiom):
  """
  rule_1 - the return value, provided that the condition chr == chr_1 is met,
  otherwise the axiom iteration is performed
  """
  return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])

def get_result(func, axiom, gens):
  """
  We form a sequence of characters for a specific generation
  """
  for gen in range(gens):
    axiom = func(axiom)
  return axiom

def draw_l_system(turtle, axiom, step,
 thickness, color, angle):
  stack = []
  for chr in axiom:
    turtle.color(color)
    if chr == 'F' or chr == 'X':
      turtle.forward(step)
    elif chr == '@':
      step -= 6
      color[1] += 0.04
      thickness -= 2
      thickness = max(1, thickness)
      turtle.pensize(thickness)
    elif chr == '+':
      turtle.right(angle())
    elif chr == '-':
      turtle.left(angle())
    elif chr == '[':
      angle_, pos_ = turtle.heading(), turtle.pos()
      stack.append((angle_, pos_, thickness, step, color[1]))
    elif chr == ']':
      angle_, pos_, thickness, step, color[1] = stack.pop()
      turtle.pensize(thickness)
      turtle.setheading(angle_)
      turtle.penup()
      turtle.goto(pos_)
      turtle.pendown()

def set_turtle(WIDTH, HEIGHT, thickness):
  r_turtle = turtle.Turtle()
  r_turtle.screen.title("L-System Derivation")
  r_turtle.pensize(3)
  r_turtle.speed(0)
  r_turtle.penup()
  r_turtle.setpos(WIDTH // 6, -HEIGHT // 4 - 25)
  r_turtle.pendown()
  r_turtle.color('green')
  
  """
  In order for the tree to grow up, you should first
  turn the turtle 90 degrees to the left
  """
  r_turtle.left(90)
  r_turtle.pensize(thickness)
  return r_turtle

# l-system settings
gens = 13
axiom = 'XY'
chr_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 85
angle = lambda: randint(0, 45)
color = [0.35, 0.2, 0.0]
thickness = 20

axiom = get_result(apply_rules, axiom, gens)

# set turtle parameters and draw L-System
WIDTH, HEIGHT = 1600, 900
r_turtle = set_turtle(WIDTH, HEIGHT, thickness)
turtle_screen = turtle.Screen()
turtle_screen.setup(WIDTH, HEIGHT)
turtle_screen.screensize(3 * WIDTH, 3 * HEIGHT)
turtle_screen.delay(0)
draw_l_system(r_turtle, axiom, step,
  thickness, color, angle)
turtle_screen.exitonclick()
