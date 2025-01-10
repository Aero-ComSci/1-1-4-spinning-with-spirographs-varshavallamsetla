import turtle

screen = turtle.Screen()
screen.setup(width=800, height=800)

def draw_objects(num_objects):
    if num_objects < 1 or num_objects > 5:
        print("Please provide a number between 1 and 5")
        return

    obj_turtle = turtle.Turtle()
    obj_turtle.shape("circle")
    obj_turtle.penup()


    screen_width = 800
    total_space = screen_width - (num_objects * 50)  
    spacing = total_space / (num_objects + 1)

    start_x = -(screen_width / 2) + spacing + 25 


    for i in range(num_objects):
        obj_turtle.goto(start_x + i * (50 + spacing), 0)
        obj_turtle.stamp() 

    obj_turtle.hideturtle()

num_objects = int(input("Enter the number of objects (1-5): "))

draw_objects(num_objects)

turtle.done()
