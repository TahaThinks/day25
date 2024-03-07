import turtle

screen = turtle.Screen()
screen.title("Taha U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="Enter a State:")
print(answer_state)

turtle.mainloop()
