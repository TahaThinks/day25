import turtle
import pandas

us_states = pandas.read_csv("50_states.csv")
# print(us_states)

us_states_list = us_states.state.tolist()
# print(us_states_list)

screen = turtle.Screen()
screen.title("Taha U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter a State:").title()
    if answer_state in us_states_list:
        print("Exists")
        desired_row = us_states[us_states["state"] == answer_state]
        x_coordinate = desired_row.x.item()
        y_coordinate = desired_row.y.item()

        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()

        turtle_state.goto(x_coordinate,y_coordinate)
        turtle_state.write(answer_state)
    else:
        print("Doesn't Exists")


turtle.mainloop()