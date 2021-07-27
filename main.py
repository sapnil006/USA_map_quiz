from pandas import *
from turtle import *

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_list = []
while len(guessed_list) < 50:
    guess = screen.textinput(title=f"{len(guessed_list)}/50 states correct)", prompt="What's "
                                                                                     "another state name").title()
    if guess == "Exit":
        # missing_states = [state for state in all_states if guess not in all_states]
        missing_states = []
        for state in all_states:
            if guess not in all_states:
                missing_states.append(state)
        new_data = DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if guess in all_states:
        guessed_list.append(guess)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == guess]  # x = data[data['state'].str.contains(guess)]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
