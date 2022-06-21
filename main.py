import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States Game")
image = "indian_locator_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states.csv")

all_states = data.state.to_list()
guessed_staes =[]

while len(guessed_staes)<38:
    answer_state = turtle.textinput(title=f"{len(guessed_staes)}/50 Correct State", prompt="What's another state name ?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_staes:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_staes.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())








