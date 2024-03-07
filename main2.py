import turtle
import pandas

us_states = pandas.read_csv("50_states.csv")
print(us_states)

us_states_list = us_states.state.tolist()
print(us_states_list)


screen = turtle.Screen()
screen.title("Taha U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while True:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter a State:")
    if answer_state.lower() in us_states_list:
        print("Exists")
    else:
        print("Doesn't Exists")


turtle.mainloop()
